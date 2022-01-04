# -*- coding: utf-8 -*-
"""
Usage :
 > python bsgs_dll_search.py -pfile 1to63_65.txt -b bpfile.bin -bl bloomfile.bin
 > python bsgs_dll_search.py -pfile Pub50.txt -b bpfile.bin -bl bloomfile.bin -rand
 > python bsgs_dll_search.py -b bpfile.bin -bl bloomfile.bin -rand1 -p 02CEB6CBBCDBDF5EF7150682150F4CE2C6F4807B349827DCDBDD1F2EFA885A2630 -keyspace 800000000000000000000000000000:FFFFFFFFFFFFFFFFFFFFFFFFFFFFFF -n 500000000000000

@author: iceland
@credits: Alberto, KV
"""
import time
import random
import bit
import os
import math
import sys
import argparse
import secp256k1 as ice


parser = argparse.ArgumentParser(description='This tool use bsgs algo for sequentially searching all pubkeys (together) in the given range', 
                                 epilog='Enjoy the program! :)    Tips BTC: bc1q39meky2mn5qjq704zz0nnkl0v7kj4uz6r529at \
                                 \nThanks a lot to AlbertoBSD Tips BTC: 1ABSD1rMTmNZHJrJP8AJhDNG1XbQjWcRz7')
parser.version = '02012022'
parser.add_argument("-pfile", "--pfile", help = "Public Key in hex format (compressed or uncompressed) line by line", action="store")
parser.add_argument("-xfile", "--xfile", help = "xpoint in hex format line by line. Both 02 & 03 will be considered automatically", action="store")
parser.add_argument("-p", "--pubkey", help = "Public Key in hex format (compressed or uncompressed)", action="store")
parser.add_argument("-b", "--bpfile", help = "Baby Point file. created using bsgs_create_bpfile_bloomfile.py", required=True)
parser.add_argument("-bl", "--bloomfile", help = "Bloom filter file. created using bsgs_create_bpfile_bloomfile.py", required=True)
parser.add_argument("-n", help = "Total sequential search in 1 loop. default=10000000000000000/No_of_Pubkeys", action='store')
parser.add_argument("-keyspace", help = "Keyspace Range ( hex ) to search from min:max. default=1:order of curve", action='store')
parser.add_argument("-rand", help = "Start from a random value in the given range from min:max and search n values then again take a new random", action="store_true")
parser.add_argument("-rand1", help = "First Start from a random value, then go fully sequential, in the given range from min:max", action="store_true")

if len(sys.argv)==1:
    parser.print_help()
    sys.exit(1)
args = parser.parse_args()


#seq = int(args.n) if args.n else 8000000000  # Approx (10000 Trillion / number of pubkeys)
ss = args.keyspace if args.keyspace else '1:FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364140'
flag_random = True if args.rand else False
flag_random1 = True if args.rand1 else False
bs_file = args.bpfile       # 'FULLbpfile.bin'
bloom_file = args.bloomfile # 'Big_dll_bloom.bin'
public_key_file = args.pfile if args.pfile else ''
xpoint_file = args.xfile if args.xfile else ''
public_key = args.pubkey if args.pubkey else ''
if flag_random1: flag_random = True
if public_key_file == '' and xpoint_file == '' and public_key == '': 
    print('One of the required option missing -pfile or -xfile or -p'); sys.exit(1)
###############################################################################
a, b = ss.split(':')
a = int(a, 16)
b = int(b, 16)


if os.path.isfile(bloom_file) == False:
    print('File {} not found'.format(bloom_file))
    print('create it from : bsgs_create_bpfile_bloomfile.py')
    sys.exit()
if os.path.isfile(bs_file) == False:
    print('File {} not found'.format(bs_file))
    print('Specify the input file used to create the bloom filter or create it from : bsgs_create_bpfile_bloomfile.py. Even little smaller file is OK.')
    sys.exit()
if os.path.isfile(public_key_file) == False and public_key_file != '':
    print('File {} not found'.format(public_key_file))
    print('1 pubkey per line in hex format,  in the file (compressed or uncompressed)')
    sys.exit()
if os.path.isfile(xpoint_file) == False and xpoint_file != '':
    print('File {} not found'.format(xpoint_file))
    print('1 xpoint per line in hex format,  in the file.')
    sys.exit()
# ======== 1st Part : File ===============

# m = math.floor(math.sqrt(k2-k1))
m_bb = int((os.stat(bs_file).st_size)/32)      # each xpoint is 32 bytes in the file
lastitem = 0


###############################################################################

# Very Very Slow. Made only to get a random number completely non pseudo stl.
def randk(a, b):
    if flag_random:
        dd = list(str(random.randint(1,2**256)))
        random.shuffle(dd); random.shuffle(dd)
        rs = int(''.join(dd))
        random.seed(rs)
        return random.SystemRandom().randint(a, b)
    else:
        if lastitem == 0:
            return a
        elif lastitem > b:
            print('[+] Range Finished')
            exit()
        else:
            return lastitem + 1

def scan_str(num):
	# Kilo/Mega/Giga/Tera/Peta/Exa/Zetta/Yotta
    dict_suffix = {0:'', 1:'KiloKeys', 2:'MegaKeys', 3:'GigaKeys', 4:'TeraKeys', 5:'PetaKeys', 6:'ExaKeys'}
    num *= 1.0
    idx = 0
    for ii in range(len(dict_suffix)-1):
        if int(num/1000) > 0:
            idx += 1
            num /= 1000
    return ('%.5f '%num)+dict_suffix[idx]
    

# =============================================================================

def pub2upub(pub_hex):
	x = int(pub_hex[2:66],16)
	if len(pub_hex) < 70:
		y = bit.format.x_to_y(x, int(pub_hex[:2],16)%2)
	else:
		y = int(pub_hex[66:],16)
	return bytes.fromhex('04'+ hex(x)[2:].zfill(64) + hex(y)[2:].zfill(64))

def read_pubkey_file():
    publist = [line.split()[0] for line in open(public_key_file,'r')]
    return publist

def read_xpoint_file():
    # use both 02 & 03 type xpoint
    publist = ['02'+line.split()[0] for line in open(xpoint_file,'r')]
    publist.extend( ['03'+line.split()[0] for line in open(xpoint_file,'r')] )
    return publist

def read_FULL_baby_file(num_bytes):
#    a = array('B')
#    elem = int((os.stat(bs_file).st_size)/3)
    with open(bs_file,'rb') as f:
        a = bytearray(f.read(num_bytes))
#        a.fromfile(f, elem)
    return a

def bloom_read_dll_from_file():
    with open(bloom_file,'rb') as f:
        ba_bloom2 = bytes(f.read())
#        ba_bloom2 = bytes( bytearray(f.read()) )
    return ba_bloom2


###############################################################################

st = time.time()
print('\n[+] Starting Program : BSGS mode     Version [', parser.version,']')

if public_key_file != '' and xpoint_file == '' and public_key == '':
    Qlist = [ bytes(bytearray(pub2upub(line))) for line in read_pubkey_file() ]
    print('[+] Loading {} Public Keys to search'.format(len(Qlist)))
if xpoint_file != '' and public_key == '':
    Qlist = [ bytes(bytearray(pub2upub(line))) for line in read_xpoint_file() ]
    print('[+] Loading {} Xpoints to search'.format(len(Qlist)))
if public_key != '':
    Qlist = [ bytes(bytearray(pub2upub(public_key))) ]
    print('[+] Search Started for the Public key: ',Qlist[0].hex())

###############################################################################
    
if flag_random1 == True:
    print('[+] Search Mode: Random Start then Fully sequential from it')
elif flag_random == True:
    print('[+] Search Mode: Random Start after every n sequential key search')
else:
    print('[+] Search Mode: Sequential search in the given range')
    
    
bloom_filter = bloom_read_dll_from_file()
print('[+] Reading bloom filter from file complete in : {0:.5f} sec'.format(time.time() - st))
st = time.time()
# =============================================================================
bloom_bits = len(bloom_filter)*8        # fix value. Dont change
bloom_hashes = 30                       # fix value. Dont change
bloom_prob = 0.000000001                # False Positive = 1 out of 1 billion
bloom_bpe = -(math.log(bloom_prob) / 0.4804530139182014)
m = math.floor(bloom_bits/bloom_bpe)
# =============================================================================
w = math.ceil(math.sqrt(m))         # secondary table elements needed
if w > m_bb:
    print('[*] Warning. Small bPfile found. Is it ok ? Proceeding...')
    w = m_bb
# =============================================================================
#bloom_filter_gmp = gmpy2.xmpz(int.from_bytes(bloom_filter.tobytes(), byteorder='big'))
#del bloom_filter
# =============================================================================
baby_bin = read_FULL_baby_file(w*32)
print('[+] Reading Baby table from file complete in : {0:.5f} sec'.format(time.time() - st))
st = time.time()
baby_dict = {sys.intern(baby_bin[i*32:i*32+32].hex()):i for i in range(w)}

###############################################################################
seq = int(args.n) if args.n else (m*5000000)//len(Qlist)  # Approx (10000 Trillion / number of pubkeys)
###############################################################################

# We have to solve P = k.G, we know that k lies in the range ]k1,k2]
k1 = randk(a, b) # start from
k2 = k1 + seq

# Reset the flag after getting 1st Random Start Key
if flag_random1 == True: flag_random = False

print('[+] seq value:',seq,'   m value :' , m)
print('[+] Search Range:',hex(a),' to ', hex(b))
###############################################################################


print('                                                                [+] k1:', hex(k1))


k1G = ice.scalar_multiplication(k1)
mG = ice.scalar_multiplication(m)
mGneg = ice.point_negation(mG)
ice.init_P2_Group(mGneg)    # make a CPU_GROUP/2 Table for mGneg
wG = ice.scalar_multiplication(w)

st = time.time()

###############################################################################

def bsgs_exact_key(pubkey_point, z1, z2):
    z1G = ice.scalar_multiplication(z1)
    if z1G == pubkey_point:
        print('============== KEYFOUND ==============')
        print('BSGS FOUND PrivateKey ', hex(z1))
        print('======================================')
        with open('KEYFOUNDKEYFOUND.txt','a') as fw:
            fw.write('BSGS_FOUND_PrivateKey '+hex(z1)+'\n')
        return True
    S = ice.point_subtraction(pubkey_point, z1G)
    
    S2_list = ice.point_loop_subtraction( 1+(k2-k1)//m, S, wG )
    curr_byte_pos = 0
    hex_line = S[1:33]
    
    stp = 0
#    print('[*] Bloom collision... Checking inside the bPfile Now... ')
    while stp<(1+z2-z1):
        idx = baby_dict.get(hex_line.hex())
        if idx is not None and idx >= 0:
#            kk = z1+stp+int(idx/32)+1
            kk = z1+stp+idx+1
#            print('[*] Bloom collision and bPfile collision... Final check for the key', hex(kk))
            if ice.scalar_multiplication(kk) == pubkey_point:
                print('============== KEYFOUND ==============')
                print('BSGS FOUND PrivateKey ',hex(kk))
                print('======================================')
                with open('KEYFOUNDKEYFOUND.txt','a') as fw:
                    fw.write('BSGS_FOUND_PrivateKey '+hex(kk)+'\n')
                return True
            elif ice.scalar_multiplication(z1+stp+w+w-idx+1) == pubkey_point:
                print('============== KEYFOUND ==============')
                print('BSGS FOUND PrivateKey ',hex(z1+stp+w+w-idx+1))
                print('======================================')
                with open('KEYFOUNDKEYFOUND.txt','a') as fw:
                    fw.write('BSGS_FOUND_PrivateKey '+hex(z1+stp+w+w-idx+1)+'\n')
                return True
            else:
                stp = stp + w
                
        else:
            # Giant step
            stp = stp + w
        
        hex_line = S2_list[curr_byte_pos+1:curr_byte_pos+33]
        curr_byte_pos += 65

# Removed from Public Confusion :(
#    print('[-] A False collision ignored. Bloom collision, but No bPfile collision.')
    return False

#################################

def bsgs_keys(pubkey_point, k1, k2):
    found = False
    if pubkey_point == k1G:
        print('============== KEYFOUND ==============')
        print('BSGS FOUND PrivateKey ', hex(k1))
        print('======================================')
        with open('KEYFOUNDKEYFOUND.txt','a') as fw:
            fw.write('BSGS_FOUND_PrivateKey '+hex(k1)+'\n')
        found = True
        return found
    
    if k1 < w:
        idx = baby_dict.get(pubkey_point[1:33].hex())
        if idx is not None and idx >= 0:
            print('============== KEYFOUND ==============')
            print('BSGS FOUND PrivateKey ', hex(idx+1))
            print('======================================')
            with open('KEYFOUNDKEYFOUND.txt','a') as fw:
                fw.write('BSGS_FOUND_PrivateKey '+hex(idx+1)+'\n')
            found = True
            return found
    
    S = ice.point_subtraction(pubkey_point, k1G)

    S_list = ice.point_sequential_increment_P2(1+(k2-k1)//m, S)
#    S_list = ice.point_loop_subtraction(1+(k2-k1)//m, S, mG)
    curr_byte_pos = 0
    hex_line = S[1:33]
    
    
    found = False
    step = 0
	
    while found is False and step<(1+k2-k1):
        if ice.ice.bloom_check_add(hex_line, 32, 0, bloom_bits, bloom_hashes, bloom_filter) > 0:
            rt = bsgs_exact_key(pubkey_point, k1+step, k1+step+m)
            if rt == True:
                return True

            step = step + m
            
# =============================================================================

        else: # Giant step
            step = step + m
        
        hex_line = S_list[curr_byte_pos+1:curr_byte_pos+33]
        curr_byte_pos += 65
        
            
    return found

# =============================================================================
if seq < m: seq = m
# =============================================================================
##################################################################
# Main Script Starting Below
##################################################################
el = 0
while True:
    found_list = []
    for Q in Qlist:
        found = bsgs_keys(Q, k1, k2)
        if found == True:
            found_list.append(Q)
#            print("Removed Found Q from Search   ")
            el = time.time() - st

    for line in found_list:
        del Qlist[Qlist.index(line)]
    if len(Qlist) == 0:
        print("Search Finished. All pubkeys Found !")
        exit()
    else:
        curr = time.time() - st
        el += curr
        lastitem = k2
        k1 = randk(a, b)
        print('PVK not found. {0} scanned in {1:.2f} sec. New range [+] k1: {2}'.format(scan_str(seq), curr, hex(k1)))
        st = time.time()
        k2 = k1 + seq
        k1G = ice.scalar_multiplication(k1)

print("Time Spent : {0:.5f} seconds".format(el))
