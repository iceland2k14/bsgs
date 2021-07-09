# -*- coding: utf-8 -*-
"""
Create bpfile.bin using multi_cpu

Usage :
 > python create_bPfile_mcpu2.py 400000000 bpfile.bin 4

@author: iceland
"""
import sys
import time
import ctypes
import os
import platform
from itertools import islice 
import math
from multiprocessing import Pool


if platform.system().lower().startswith('win'):
    pathdll = os.path.realpath('ice_secp256k1.dll')
    ice = ctypes.CDLL(pathdll)
    
elif platform.system().lower().startswith('lin'):
    pathdll = os.path.realpath('ice_secp256k1.so')
    ice = ctypes.CDLL(pathdll)
    
else:
    print('[-] Unsupported Platform currently for ctypes dll method. Only [Windows and Linux] is working')
    sys.exit()
    

ice.scalar_multiplication.argtypes = [ctypes.c_char_p, ctypes.c_char_p]            # pvk,ret
ice.point_increment.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p] # x,y,ret
ice.point_negation.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]  # x,y,ret
ice.create_baby_table.argtypes = [ctypes.c_ulonglong, ctypes.c_ulonglong, ctypes.c_char_p] # start,end,ret
ice.point_addition.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
ice.point_subtraction.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]

ice.init_secp256_lib()


def scalar_multiplication(kk):
    res = (b'\x00') * 65
    pass_int_value = hex(kk)[2:].encode('utf8')
    ice.scalar_multiplication(pass_int_value, res)
    return res

def point_increment(pubkey_bytes):
    x1 = pubkey_bytes[1:33]
    y1 = pubkey_bytes[33:]
    res = (b'\x00') * 65
    ice.point_increment(x1, y1, res)
    return res

def point_negation(pubkey_bytes):
    x1 = pubkey_bytes[1:33]
    y1 = pubkey_bytes[33:]
    res = (b'\x00') * 65
    ice.point_negation(x1, y1, res)
    return res

def create_baby_table(start_value, end_value):
    res = (b'\x00') * ((1+end_value-start_value) * 32)
    ice.create_baby_table(start_value, end_value, res)
    return res

def point_addition(pubkey1_bytes, pubkey2_bytes):
    x1 = pubkey1_bytes[1:33]
    y1 = pubkey1_bytes[33:]
    x2 = pubkey2_bytes[1:33]
    y2 = pubkey2_bytes[33:]
    res = (b'\x00') * 65
    ice.point_addition(x1, y1, x2, y2, res)
    return res

def point_subtraction(pubkey1_bytes, pubkey2_bytes):
    x1 = pubkey1_bytes[1:33]
    y1 = pubkey1_bytes[33:]
    x2 = pubkey2_bytes[1:33]
    y2 = pubkey2_bytes[33:]
    res = (b'\x00') * 65
    ice.point_subtraction(x1, y1, x2, y2, res)
    return res

###############################################################################

def create_table(this_list):
    start_value, end_value, m = this_list
    print('[+] Working on Chunk {} ...'.format(m))
    baby_steps = create_baby_table(start_value, end_value)
    return baby_steps

def table_wrapper(data):
    create_table(*data)     
# =============================================================================
if __name__ == '__main__':
    if len(sys.argv) > 4 or len(sys.argv) < 4:
        print('[+] Program Usage.... ')
        print('{} <bP items> <output filename> <Number of cpu>\n'.format(sys.argv[0]))
        print('Example to create a File with 400 million items using 4 cpu:\n{} 400000000 bpfile.bin 4'.format(sys.argv[0]))
        sys.exit()

    st = time.time()
    total = int(sys.argv[1])
    bs_file = sys.argv[2]
    num_cpu = int(sys.argv[3])
    out = open(bs_file, 'wb')
    chunk = 10000000
    print('\n[+] Program Running please wait...')
    print('[+] Each chunk size :', chunk)
    
    seq = range(1, total+1)
    parts_list = [seq[i * chunk:(i * chunk) + chunk] for i in range(math.ceil(len(seq) / chunk))]
    print('[+] Created Total {} Chunks ...'.format(len(parts_list)))
    
    parts_list = [(min(line), max(line), k+1) for k, line in enumerate(parts_list)]
    nn = iter(parts_list)
    subdata = [list(islice(nn, num_cpu)) for m in range((len(parts_list)//num_cpu)+1)]
    
    k = 1
    
    while k <= len(subdata):
        
        pool = Pool(processes=num_cpu)
        results = pool.map(create_table, subdata[k-1])
            
        for mm in range(len(results)):
            out.write(results[mm])
            out.flush()
            os.fsync(out.fileno())
        pool.close()
        
        k += 1
        
        
    out.close()
    print('[+] File created successfully\n')
    print('[-] Completed in {0:.2f} sec'.format(time.time() - st))