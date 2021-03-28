# -*- coding: utf-8 -*-
"""
Usage :
 > python bsgs_hybrid_gmp.py -pfile 50BTC_Address_Coinbase_Sochain_Pubkey.txt -b FULLbpfile.bin -bl Bigbloomfilter.bin -n 8000000000 -keyspace 800000000000000000000000000000:FFFFFFFFFFFFFFFFFFFFFFFFFFFFFF -rand

@author: iceland
"""
import time
import random
# import gmpy2
import bit
import os
import math
import sys
import argparse
from bitarray import bitarray
import xxhash
import gmp_ec as ec

parser = argparse.ArgumentParser(description='This tool use bsgs algo for sequentially searching all pubkeys (together) in the given range', 
                                 epilog='Enjoy the program! :)    Tips BTC: bc1q39meky2mn5qjq704zz0nnkl0v7kj4uz6r529at \
                                 \nThanks a lot to AlbertoBSD Tips BTC: 1ABSD1rMTmNZHJrJP8AJhDNG1XbQjWcRz7')
parser.version = '28032021'
parser.add_argument("-pfile", "--pfile", help = "Public Key in hex format (compressed or uncompressed) line by line", required=True)
parser.add_argument("-b", "--bpfile", help = "Baby Point file. created using create_bPfile.py", required=True)
parser.add_argument("-bl", "--bloomfile", help = "Bloom filter file. created using bPfile_2_bloom.py", required=True)
parser.add_argument("-n", help = "Total sequential search in 1 loop. default=20000000000000", action='store')
parser.add_argument("-keyspace", help = "Keyspace Range ( hex ) to search from min:max. default=1:order of curve / 2", action='store')
parser.add_argument("-rand", help = "Start from a random value in the given range from min:max", action="store_true")

if len(sys.argv)==1:
    parser.print_help()
    sys.exit(1)
args = parser.parse_args()


seq = int(args.n) if args.n else 8000000000
ss = args.keyspace if args.keyspace else '1:7FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF5D576E7357A4501DDFE92F46681B20A0'
flag_random = True if args.rand else False
bs_file = args.bpfile       # 'FULLbpfile.bin'
bloom_file = args.bloomfile # 'FULLbloomfilter.bin'
public_key_file = args.pfile    # '02CEB6CBBCDBDF5EF7150682150F4CE2C6F4807B349827DCDBDD1F2EFA885A2630'
###############################################################################
a, b = ss.split(':')
a = int(a, 16)
b = int(b, 16)


if os.path.isfile(bloom_file) == False:
    print('File {} not found'.format(bloom_file))
    print('create it from : bPfile_2_bloom.py')
    sys.exit()
if os.path.isfile(bs_file) == False:
    print('File {} not found'.format(bs_file))
    print('Specify the file used to create the bloom filter or create it from : create_bPfile.py. Even little smaller file is OK.')
    sys.exit()
if os.path.isfile(public_key_file) == False:
    print('File {} not found'.format(public_key_file))
    print('1 pubkey per line in hex format,  in the file (compressed or uncompressed)')
    sys.exit()
# ======== 1st Part : File ===============
N2 = 0X7FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF5D576E7357A4501DDFE92F46681B20A0

# m = 40000000     # m = math.floor(math.sqrt(k2-k1))
m_bb = int((os.stat(bs_file).st_size)/32)      # each xpoint is 32 bytes in the file
lastitem = 0

###############################################################################
def randk(a, b):
	if flag_random:
		return random.SystemRandom().randint(a, b)
	else:
		if lastitem == 0:
			return a
		else:
			return lastitem + 1

def scan_str(num):
	# Kilo/Mega/Giga/Tera/Peta/Exa/Zetta/Yotta
    dict_suffix = {0:'', 1:'Thousands', 2:'Million', 3:'Billion', 4:'Trillion'}
    num *= 1.0
    idx = 0
    for ii in range(4):
        if int(num/1000) > 0:
            idx += 1
            num /= 1000
    return ('%.5f '%num)+dict_suffix[idx]
    
def pub2point(pub_hex):
	x = int(pub_hex[2:66],16)
	if len(pub_hex) < 70:
		y = bit.format.x_to_y(x, int(pub_hex[:2],16)%2)
	else:
		y = int(pub_hex[66:], 16)
	return ec.Point(x, y)

def read_pubkey_file():
    publist = [line.split()[0] for line in open(public_key_file,'r')]
    return publist

def read_FULL_baby_file(num_bytes):
#    a = array('B')
#    elem = int((os.stat(bs_file).st_size)/3)
    with open(bs_file,'rb') as f:
        a = bytearray(f.read(num_bytes))
#        a.fromfile(f, elem)
    return a

def bloom_read_from_file():
    a = bitarray()
    with open(bloom_file, 'rb') as fh:
        a.fromfile(fh)
    return a

def check_in_bloom(positions, bloom_bits, bitarr):
    flag = True
    for loc in positions:
        if bitarr[loc] == 0 : flag = False
#        loc1 = bloom_bits-loc-1
#        if bitarr[loc1] == 0 : flag = False
    return flag

def hashit(dn, bloom_hashes, bloom_bits):
    a = int(xxhash.xxh64_hexdigest(dn, seed=0),16)
    b = int(xxhash.xxh64_hexdigest(dn, seed=a),16)
    idx = [(a + b * k)%bloom_bits for k in range(bloom_hashes)]  # get int for bit setting
    return idx
###############################################################################

st = time.time()
print('[+] Starting Program : BSGS mode with hybrid algo using bloom')
Qlist = [ pub2point(line) for line in read_pubkey_file() ]
print('[+] Loading {} Public Keys to search'.format(len(Qlist)))
# Q = pub2point(public_key)

bloom_filter = bloom_read_from_file()
print('[+] Reading bloom filter from file complete in : {0:.5f} sec'.format(time.time() - st))
st = time.time()
# =============================================================================
bloom_bits = len(bloom_filter)          # 862655256        # fix value. Dont change
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
# baby_steps = [baby_bin[cnt*32:cnt*32+32].hex() for cnt in range(w)]
# baby_steps = {int(line,10):k for k, line in enumerate(baby_steps)}
# baby_steps = set(baby_steps)
# =============================================================================

# We have to solve P = k.G, we know that k lies in the range ]k1,k2]
k1 = randk(a, b) # start from
k2 = k1 + seq


print('[+] seq value:',seq,'   m value :' , m)
G = ec.G
Zp = ec.Point.IDENTITY_ELEMENT
print('[+] Search Range:',hex(a),' to ', hex(b))
###############################################################################


print('                                                                [+] k1:', hex(k1))


k1G = ec.Scalar_Multiplication(k1, G)
mG = ec.Scalar_Multiplication(m, G)

st = time.time()

###############################################################################

def bsgs_exact_key(pubkey_point, z1, z2):
    z1G = z1 * G
    wG = w * G
    S = pubkey_point -z1G
    if S == Zp:
        if z1 * G == pubkey_point:
            print('BSGS FOUND PrivateKey ', hex(z1))
            return True
    stp = 0
    while stp<(1+z2-z1):
        hex_line = hex(S.x)[2:].zfill(64)
        idx = baby_bin.find(bytes.fromhex(hex_line), 0)
        if idx > 0:
            kk = z1+stp+int(idx/32)+1
            if kk * G == pubkey_point:
                print('============== KEYFOUND ==============')
                print('BSGS FOUND PrivateKey ',hex(kk))
                print('======================================')
                return True
            else:
                S = S - wG
                stp = stp + w
                
        else:
            # Giant step
            S = S - wG
            stp = stp + w
    print('A False collision ignored')
    return False

#################################

def bsgs_keys(pubkey_point, k1, k2):
    found = False
    S = ec.Point_Addition(pubkey_point, -k1G)
    if S == Zp:
        print('BSGS FOUND PrivateKey ', hex(k1))
        found = True
        return found
    
    found = False
    step = 0
	
    while found is False and step<(1+k2-k1):
        hex_line = hex(S.x)[2:].zfill(64)
        if check_in_bloom(hashit(hex_line, bloom_hashes, bloom_bits), bloom_bits, bloom_filter) == True:
            rt = bsgs_exact_key(pubkey_point, k1+step, k1+step+m)
            if rt == True:
                return True
#            print('A False collision ignored between ',hex(k1+step), ' and ', hex(k1+step+m))
            S = ec.Point_Addition(S, -mG)
            step = step + m
            
# =============================================================================

        else: # Giant step
            S = ec.Point_Addition(S, -mG)
            step = step + m
            
    return found

# =============================================================================
    
el = 0
while True:
    found_list = []
    for Q in Qlist:
        found = bsgs_keys(Q, k1, k2)
        if found == True:
            found_list.append(Q)
            print("Removed Found Q from Search   ")
            el = time.time() - st
            #break
    for line in found_list:
        del Qlist[Qlist.index(line)]
    if len(Qlist) == 0:
        print("Search Finished. All pubkeys Found !")
    else:
        curr = time.time() - st
        el += curr
        lastitem = k2
        k1 = randk(a, b)
        print('PVK not found. {0} scanned in {1:.2f} sec. New range [+] k1: {2}'.format(scan_str(seq), curr, hex(k1)))
        st = time.time()
        k2 = k1 + seq
        k1G = ec.Scalar_Multiplication(k1, G)
#        print('[+] k1:', hex(k1))
print("Time Spent : {0:.5f} seconds".format(el))
