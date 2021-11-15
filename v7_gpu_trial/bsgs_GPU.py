# -*- coding: utf-8 -*-
"""
Usage :
 > python bsgs_GPU.py -pubkey 02CEB6CBBCDBDF5EF7150682150F4CE2C6F4807B349827DCDBDD1F2EFA885A2630 -n 100000000000000000 -d 0 -t 256 -b 20 -p 1024 -bp 5000000 -keyspace 800000000000000000000000000000:ffffffffffffffffffffffffffffff -rand1
 
 
@author: iceland
@Credit: KanhaVishva and AlbertoBSD
"""
import secp256k1_lib as ice
import bit
import ctypes
import os
import sys
import platform
import random
import math
import signal
import argparse
#from numba import cuda 

#==============================================================================
parser = argparse.ArgumentParser(description='This tool use bsgs algo for sequentially searching 1 pubkey in the given range', 
                                 epilog='Enjoy the program! :)    Tips BTC: bc1q39meky2mn5qjq704zz0nnkl0v7kj4uz6r529at \
                                 \nThanks a lot to AlbertoBSD and KanhaVishva for their help.')
parser.version = '15112021'
parser.add_argument("-pubkey", help = "Public Key in hex format (compressed or uncompressed)", action="store", required=True)
parser.add_argument("-n", help = "Total sequential search in 1 loop. default=10000000000000000", action='store')
parser.add_argument("-d", help = "GPU Device. default=0", action='store')
parser.add_argument("-t", help = "GPU Threads. default=256", action='store')
parser.add_argument("-b", help = "GPU Blocks. default=20", action='store')
parser.add_argument("-p", help = "GPU Points per Threads. default=256", action='store')
parser.add_argument("-bp", help = "bP Table Elements for GPU. default=2000000", action='store')
parser.add_argument("-keyspace", help = "Keyspace Range ( hex ) to search from min:max. default=1:order of curve", action='store')
parser.add_argument("-rand", help = "Start from a random value in the given range from min:max and search n values then again take a new random", action="store_true")
parser.add_argument("-rand1", help = "First Start from a random value, then go fully sequential, in the given range from min:max", action="store_true")

if len(sys.argv)==1:
    parser.print_help()
    sys.exit(1)
args = parser.parse_args()
#==============================================================================

seq = int(args.n) if args.n else 10000000000000000  # 10000 Trillion
ss = args.keyspace if args.keyspace else '1:FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364140'
flag_random = True if args.rand else False
flag_random1 = True if args.rand1 else False
gpu_device = int(args.d) if args.d else 0
gpu_threads = int(args.t) if args.t else 256
gpu_blocks = int(args.b) if args.b else 20
gpu_points = int(args.p) if args.p else 256
bp_size = int(args.bp) if args.bp else 2000000
public_key = args.pubkey if args.pubkey else '02e9dd713a2f6c4d684355110d9700063c66bc823b058e959e6674d4aa6484a585'
if flag_random1: flag_random = True

lastitem = 0
###############################################################################
a, b = ss.split(':')
a = int(a, 16)
b = int(b, 16)

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

#==============================================================================
gpu_bits = int(math.log2(bp_size))
#==============================================================================

def pub2upub(pub_hex):
	x = int(pub_hex[2:66],16)
	if len(pub_hex) < 70:
		y = bit.format.x_to_y(x, int(pub_hex[:2],16)%2)
	else:
		y = int(pub_hex[66:],16)
	return bytes.fromhex('04'+ hex(x)[2:].zfill(64) + hex(y)[2:].zfill(64))

#==============================================================================
    
print('\n[+] Starting Program.... Please Wait !')
if flag_random1 == True:
    print('[+] Search Mode: Random Start then Fully sequential from it')
elif flag_random == True:
    print('[+] Search Mode: Random Start after every n sequential key search')
else:
    print('[+] Search Mode: Sequential search in the given range')

k1 = randk(a, b) # start from
k2 = k1 + seq

# Reset the flag after getting 1st Random Start Key
if flag_random1 == True: flag_random = False
#==============================================================================
P = pub2upub(public_key)
G = ice.scalar_multiplication(1)
P3 = ice.point_loop_addition(bp_size, P, G)
#==============================================================================
if platform.system().lower().startswith('win'):
    dllfile = 'bt2.dll'
    if os.path.isfile(dllfile) == True:
        pathdll = os.path.realpath(dllfile)
        bsgsgpu = ctypes.CDLL(pathdll)
    else:
        print('File {} not found'.format(dllfile))
    
elif platform.system().lower().startswith('lin'):
    dllfile = 'bt2.so'
    if os.path.isfile(dllfile) == True:
        pathdll = os.path.realpath(dllfile)
        bsgsgpu = ctypes.CDLL(pathdll)
    else:
        print('File {} not found'.format(dllfile))
        
else:
    print('[-] Unsupported Platform currently for ctypes dll method. Only [Windows and Linux] is working')
    sys.exit()
    
bsgsgpu.bsgsGPU.argtypes = [ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int, ctypes.c_char_p, ctypes.c_uint32, ctypes.c_char_p, ctypes.c_char_p] # t,b,p,rb,dv,upubs,size,keyspace,bp
bsgsgpu.bsgsGPU.restype = ctypes.c_void_p
bsgsgpu.free_memory.argtypes = [ctypes.c_void_p] # pointer
#==============================================================================

while True:
#    device = cuda.get_current_device()
#    device.reset()
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    st_en = hex(k1)[2:] +':'+ hex(k2)[2:]
    res = bsgsgpu.bsgsGPU(gpu_threads, gpu_blocks, gpu_points, gpu_bits, gpu_device, P3, len(P3)//65, st_en.encode('utf8'), str(bp_size).encode('utf8'))
    pvk = (ctypes.cast(res, ctypes.c_char_p).value).decode('utf8')
    bsgsgpu.free_memory(res)
    
    if pvk != '':
        print('Magic:  ', pvk)
        foundpub = bit.Key.from_int(int(pvk, 16)).public_key
        idx = P3.find(foundpub[1:33], 0)
#==============================================================================
        if idx >=0:
            BSGS_Key = int(pvk, 16) - (((idx-1)//65)+1)
            print('============== KEYFOUND ==============')
            print('BSGS FOUND PrivateKey ',hex(BSGS_Key))
            print('======================================')
            break
        else:
            print('Something is wrong. Please check ! [idx=', idx,']')
    
    lastitem = k2
    k1 = randk(a, b)
    k2 = k1 + seq
print('Program Finished.')