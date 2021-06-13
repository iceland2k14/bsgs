# -*- coding: utf-8 -*-
"""
read bPtable and save to bloomfilter

Usage :
 > python bPfile_2_bloom_dll_batch.py FULLbpfile.bin FULL_dll_bloom.bin

@author: iceland
"""

import time
import os
import sys
import ctypes
import platform
import math


if len(sys.argv) > 3 or len(sys.argv) < 3:
    print('[+] Program Usage.... ')
    print('{} <input bPfile> <output bloomfile>\n'.format(sys.argv[0]))
    print('Example to create a File :\n{} FULLbpfile.bin FULL_dll_bloom.bin'.format(sys.argv[0]))
    sys.exit()


if platform.system().lower().startswith('win'):
    mylib = ctypes.CDLL('bloom_batch.dll')
    
elif platform.system().lower().startswith('lin'):
    mylib = ctypes.CDLL('./bloom_batch.so')
    
else:
    print('[-] Unsupported Platform currently for ctypes dll method. Only [Windows and Linux] is working')
    sys.exit()

bloom_check_add = mylib.bloom_check_add
bloom_check_add.restype = ctypes.c_int
bloom_check_add.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_ulonglong, ctypes.c_ubyte, ctypes.c_char_p]

bloom_batch_add = mylib.bloom_batch_add
bloom_batch_add.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int, ctypes.c_int, ctypes.c_ulonglong, ctypes.c_ubyte, ctypes.c_char_p]

st = time.time()
# =============================================================================
input_bPfile = sys.argv[1]              # input_bPfile = 'FULLbpfile.bin'
output_bloomfile = sys.argv[2]          # output_bloomfile = 'FULLbloomfilter.bin'

# =============================================================================
total_entries = int((os.stat(input_bPfile).st_size)/32)             #400000000
# =============================================================================

bloom_prob = 0.000000001                # False Positive = 1 out of 1 billion
bloom_bpe = -(math.log(bloom_prob) / 0.4804530139182014)

bloom_bits = int(total_entries * bloom_bpe)  # ln(2)**2
if bloom_bits % 8: bloom_bits = 8*(1 + (bloom_bits//8))
bloom_hashes = math.ceil(0.693147180559945 * bloom_bpe)

print('bloom bits  :', bloom_bits, '   size [%s MB]'%(bloom_bits//(8*1024*1024)))
print('bloom hashes:', bloom_hashes)
# =============================================================================

print('[+] Initializing the bloom filters to null')
bloom_filter = bytes(b'\x00') * (bloom_bits//8)
# =============================================================================

# =============================================================================
def bloombytes_save_to_file(ba_bloom):
    with open(output_bloomfile, 'wb') as fh:
        fh.write(ba_bloom)
        
# =============================================================================
print('[+] Reading Baby table from file ',total_entries,' elements')
f = open(input_bPfile,'rb')

# ==============Compromize Speed with RAM : Use for normal case ==============
seq = range(0, total_entries)
chunk = 1000000
parts_list = [seq[i * chunk:(i * chunk) + chunk] for i in range(math.ceil(len(seq) / chunk))]
print('[+] Created {} Chunks ...'.format(len(parts_list)))
k = 1
print('[+] Inserting baby table elements in bloom filter: Updating bloom in chunks')

while True:
    baby_bin = bytes(f.read(chunk*32))
    if not baby_bin: break
    print('[+] Working on Chunk {} ...'.format(k), end='\r')
    
    cnt = len(baby_bin)//32     # This takes care of the last part with less than chunk items
    bloom_batch_add(cnt, baby_bin, 32, 1, bloom_bits, bloom_hashes, bloom_filter)
        
    k += 1
    


# =============================================================================
print('[+] Freeing some memory             ')
del baby_bin

print('[+] Saving bloom filter to file')
bloombytes_save_to_file(bloom_filter)
print('[-] Completed in {0:.2f} sec'.format(time.time() - st))
# print(f"{' ':<60}{time.time() - st:>10}")