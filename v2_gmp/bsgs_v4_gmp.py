# -*- coding: utf-8 -*-
"""
Usage :
 > python bsgs_v4_gmp.py -p 02CEB6CBBCDBDF5EF7150682150F4CE2C6F4807B349827DCDBDD1F2EFA885A2630 -b FULLbpfile.bin -n 20000000000000 -keyspace 800000000000000000000000000000:FFFFFFFFFFFFFFFFFFFFFFFFFFFFFF -rand

@author: iceland
"""
import time
import random
import gmp_ec as ec
import bit
import os
import sys
import argparse


parser = argparse.ArgumentParser(description='This tool use bsgs algo for sequentially searching 1 pubkey in the given range', epilog='Enjoy the program! :)    Tips: bc1q39meky2mn5qjq704zz0nnkl0v7kj4uz6r529at')
parser.version = '11022021'
parser.add_argument("-p", "--pubkey", help = "Public Key in hex format (compressed or uncompressed)", required=True)
parser.add_argument("-b", "--bpfile", help = "Baby Point file. created using create_bPfile.py", required=True)
parser.add_argument("-n", help = "Total sequential search in 1 loop. default=20000000000000", action='store')
parser.add_argument("-keyspace", help = "Keyspace Range ( hex ) to search from min:max. default=1:order of curve / 2", action='store')
parser.add_argument("-rand", help = "Start from a random value in the given range from min:max", action="store_true")

if len(sys.argv)==1:
    parser.print_help()
    sys.exit(1)
args = parser.parse_args()


seq = int(args.n) if args.n else 20000000000000
ss = args.keyspace if args.keyspace else '1:7FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF5D576E7357A4501DDFE92F46681B20A0'
flag_random = True if args.rand else False
bs_file = args.bpfile       # 'bPfile.bin'
public_key = args.pubkey    # '02CEB6CBBCDBDF5EF7150682150F4CE2C6F4807B349827DCDBDD1F2EFA885A2630'
###############################################################################
a, b = ss.split(':')
a = int(a, 16)
b = int(b, 16)


if os.path.isfile(bs_file) == False:
    print('File {} not found'.format(bs_file))
    print('create it from : create_bPfile.py')
    sys.exit()
# ======== 1st Part : File ===============
N2 = 0X7FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF5D576E7357A4501DDFE92F46681B20A0

# m = 40000000     # m = math.floor(math.sqrt(k2-k1))
m = int((os.stat(bs_file).st_size)/32)      # each xpoint is 32 bytes in the file
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


def read_FULL_baby_file():
#    a = array('B')
#    elem = int((os.stat(bs_file).st_size)/3)
    with open(bs_file,'rb') as f:
        a = bytearray(f.read())
#        a.fromfile(f, elem)
    return a


###############################################################################

st = time.time()
print('[+] Starting Program : BSGS mode')
Q = pub2point(public_key)


baby_bin = read_FULL_baby_file()
print('[+] Reading Baby table from file complete in : {0:.5f} sec'.format(time.time() - st))
st = time.time()
baby_steps = [baby_bin[cnt*32:cnt*32+32].hex() for cnt in range(m)]
baby_steps = set(baby_steps)

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
#################################

def bsgs_keys(pubkey_point, k1, k2):
    found = False
    S = ec.Point_Addition(pubkey_point, -k1G)
    if S == Zp:
        print('PVK found ', hex(k1))
        found = True
        return found
    
    found = False
    step = 0
	
    while found is False and step<(1+k2-k1):
        hex_line = hex(S.x)[2:].zfill(64)
        if hex_line in baby_steps:
            idx = baby_bin.find(bytes.fromhex(hex_line), 0)
            print('PVK found ', hex(k1+step+int(idx/32)+1))
            found = True
            break

        else: # Giant step
            S = ec.Point_Addition(S, -mG)
            step = step + m
            
    return found

el = 0
while True:
    found = bsgs_keys(Q, k1, k2)
    if found == True:
        print("BSGS FOUND PrivateKey   ")
        el = time.time() - st
        break
    
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
