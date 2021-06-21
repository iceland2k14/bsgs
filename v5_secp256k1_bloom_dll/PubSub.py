# -*- coding: utf-8 -*-
"""
Usage :
 > python PubSub.py 02CEB6CBBCDBDF5EF7150682150F4CE2C6F4807B349827DCDBDD1F2EFA885A2630 100000 120 keysub120.bin xpoint
 > python PubSub.py 02CEB6CBBCDBDF5EF7150682150F4CE2C6F4807B349827DCDBDD1F2EFA885A2630 100000 120 keysub120.txt upub

@author: iceland
"""
import bit
import hashlib
import random
from time import time
import os
import sys
import ctypes


if len(sys.argv) > 6 or len(sys.argv) < 6:
    print('[+] Program Usage.... ')
    print('{} <original_pubkey> <num_of_subkeys> <bit_range> <file_flag>\n'.format(sys.argv[0]))
    print('Example to create a text File [upub]:\n{} 02CEB6CBBCDBDF5EF7150682150F4CE2C6F4807B349827DCDBDD1F2EFA885A2630 100000 120 keysub120.txt upub'.format(sys.argv[0]))
    print('Example to create a binary File [xpoint]:\n{} 02CEB6CBBCDBDF5EF7150682150F4CE2C6F4807B349827DCDBDD1F2EFA885A2630 100000 120 keysub120.bin xpoint'.format(sys.argv[0]))
    sys.exit()

pubkey = sys.argv[1]
n = int(sys.argv[2])
nbits = int(sys.argv[3])
out_file = sys.argv[4]  # False if need to write Text File, line by line
out_mode = sys.argv[5]   # upub, cpub, xpoint

if out_mode not in ['upub', 'cpub', 'xpoint']: 
    print('Output Mode not specified. [upub or cpub or xpoint]'); sys.exit()

flag_binary_file = False if out_file.split('.')[1] in ['txt','text','asc'] else True
print('[+] Detecting output file extension. Output will be written as Binary File')

low = 2**(nbits-1)
high = -1+2**nbits
diff = high - low

flag_write = 'wb' if flag_binary_file else 'w'
out = open(out_file, flag_write)
###############################################################################
ice = ctypes.CDLL('ice_secp256k1.dll')
ice.scalar_multiplication.argtypes = [ctypes.c_char_p, ctypes.c_char_p]            # pvk,ret
ice.point_subtraction.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p] # x1,y1,x2,y2,ret
ice.init_secp256_lib()
###############################################################################

def scalar_multiplication(kk):
    res = (b'\x00') * 65
    pass_int_value = hex(kk)[2:].encode('utf8')
    ice.scalar_multiplication(pass_int_value, res)
    return res

def point_subtraction(pubkey1_bytes, pubkey2_bytes):
    x1 = pubkey1_bytes[1:33]
    y1 = pubkey1_bytes[33:]
    x2 = pubkey2_bytes[1:33]
    y2 = pubkey2_bytes[33:]
    res = (b'\x00') * 65
    ice.point_subtraction(x1, y1, x2, y2, res)
    return res

def new_pos(full_bytes):
    pos = hashlib.sha256(full_bytes).digest()
    return pos

def fixrange(full_bytes):
    t = low + int(full_bytes.hex(), 16) % diff
    return t

def pub2upub(pub_hex):
	x = int(pub_hex[2:66],16)
	if len(pub_hex) < 70:
		y = bit.format.x_to_y(x, int(pub_hex[:2],16)%2)
	else:
		y = int(pub_hex[66:],16)
	return bytes.fromhex('04'+ hex(x)[2:].zfill(64) + hex(y)[2:].zfill(64))

def upub2cpub(upub_bytes):
    x1 = upub_bytes[1:33]
    prefix = str(2 + int(upub_bytes[33:].hex(), 16)%2).zfill(2)
    return bytes.fromhex(prefix)+x1
###############################################################################
st = time()
P = pub2upub(pubkey)
#key_seed = bytes.fromhex(hex(random.SystemRandom().randint(1,2**256))[2:])
key_seed = b'IceLand'

if out_mode == 'upub': size_key = 65
if out_mode == 'cpub': size_key = 33
if out_mode == 'xpoint': size_key = 32

if flag_binary_file:
    if out_mode == 'upub': out.write(P)             # Write Orginal Pubkey
    if out_mode == 'cpub': out.write(upub2cpub(P))        # Write Orginal Pubkey
    if out_mode == 'xpoint': out.write(P[1:33])     # Write Orginal Pubkey
else:
    if out_mode == 'upub': out.write(P.hex() + '  # Original_Pubkey\n')
    if out_mode == 'cpub': out.write(upub2cpub(P).hex() + '  # Original_Pubkey\n')
    if out_mode == 'xpoint': out.write(P[1:33].hex() + '  # Original_Pubkey\n')
                                     

res = bytearray((b'\x00') * (size_key * n))
for m in range(n):
    key_seed = new_pos(key_seed)
    qfix = fixrange(key_seed)
    tpub = bytes(bytearray(scalar_multiplication(qfix)))
    subP = bytes(bytearray(point_subtraction(P, tpub)))
    if out_mode == 'upub':  res[m*size_key:m*size_key+size_key] = bytes(subP)
    if out_mode == 'cpub':  res[m*size_key:m*size_key+size_key] = bytes(upub2cpub(subP))
    if out_mode == 'xpoint':  res[m*size_key:m*size_key+size_key] = bytes(subP[1:33])
    if m%10000==0: print('[+] Finished Total SubKeys # ', m, end= '\r')
    if not flag_binary_file:
        if out_mode == 'upub': out.write(bytes(subP).hex() + '  # -' + str(qfix)+'\n')  # Write text file line by line
        if out_mode == 'cpub': out.write(bytes(upub2cpub(subP)).hex() + '  # -' + str(qfix)+'\n')  # Write text file line by line
        if out_mode == 'xpoint': out.write(bytes(subP[1:33]).hex() + '  # -' + str(qfix)+'\n')  # Write text file line by line

if flag_binary_file:
    out.write(res)
out.flush()
os.fsync(out.fileno())
out.close()
print('[+] Finished Total SubKeys # ', n, end= '\r')
print('[-] Completed in {0:.2f} sec'.format(time() - st))