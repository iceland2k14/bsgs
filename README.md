# bsgs
Find PrivateKey of corresponding Pubkey(s) using BSGS algo.
Python3 implementation Using 1 thread. 

## v1_fastecdsa & v2_gmp & v3_gmp_bloom
README files moved to their corresponding folders

## LATEST Version : bsgs_dll_gmp
This script uses compiled library bloom.dll / bloom.so for Windows/Linux to handle the bloom part. The efficiency is increased in creating the bloomfilter file x10 times with overall Performance increase in Key Search is x3 times.

The main script to search 1 public key using BSGS algo is bsgs_dll_gmp.py

Another script _bsgs_hybrid_dll_gmp.py_ has been include to search multiple publickeys all Together (not 1 by 1). Here the script can search millions of pubkey at once but the speed reduces quickly. Although it is still faster than searching the address or HASH160.

## Usage
- ```python create_bPfile_mcpu.py 200000000 bPfile.bin 4```  _This uses 4 cpu to make bPfile with 200 million items._
- ```python bPfile_2_bloom_dll.py bpfile.bin bloomfile.bin```    _This converts that bPfile created earlier into a bloom file._
- ```python bsgs_dll_gmp.py -p 02CEB6CBBCDBDF5EF7150682150F4CE2C6F4807B349827DCDBDD1F2EFA885A2630 -b bPfile.bin -bl bloomfile.bin -n 50000000000000 -keyspace 800000000000000000000000000000:FFFFFFFFFFFFFFFFFFFFFFFFFFFFFF -rand```   _This is the main script to search for 1 pubkey using the files created earlier._
- ```python bsgs_hybrid_dll_gmp.py -pfile Pub50.txt -b FULLbpfile.bin -bl Big5GB_dll_bloom.bin -n 8000000000 -rand1```   _This is the main script to search for multi pubkey using the files created earlier._

***Note: Think about How much RAM your system has free which you are going to allow to use in this script.
For Example 1 billion items will require 5GB bloom file and therefore 5GB for running the final script. So plan accordingly during creation of bPfile and bloomfile.***


# Run
```
(base) C:\anaconda3>python create_bPfile_mcpu.py 7000000 yybPfile.bin 4

[+] Program Running please wait...
[+] Created Total 7 Chunks ...
[+] Working on Chunk 1 ...
[+] Working on Chunk 2 ...
[+] Working on Chunk 3 ...
[+] Working on Chunk 4 ...
[+] Working on Chunk 5 ...
[+] Working on Chunk 6 ...
[+] Working on Chunk 7 ...
[+] File created successfully


(base) C:\anaconda3>python bPfile_2_bloom_dll.py yybpfile.bin yy_bloom.bin
bloom bits  : 301929344    size [35 MB]
bloom hashes: 30
[+] Initializing the bloom filters to null
[+] Reading Baby table from file  7000000  elements
[+] Created 7 Chunks ...
[+] Inserting baby table elements in bloom filter: Updating bloom in chunks
[+] Freeing some memory
[+] Saving bloom filter to file
[-] Completed in 28.27 sec


(base) C:\anaconda3>python bsgs_dll_gmp.py -p 02CEB6CBBCDBDF5EF7150682150F4CE2C6F4807B349827DCDBDD1F2EFA885A2630 -b FULLbpfile.bin -bl Big5GB_dll_bloom.bin -n 500000000000000 -keyspace 800000000000000000000000000000:FFFFFFFFFFFFFFFFFFFFFFFFFFFFFF -rand
[+] Starting Program : BSGS mode
[+] Searching Started for the Public key
[+] Search Mode: Random Start after every n sequential key search
[+] Reading bloom filter from file complete in : 2.64984 sec
[+] Reading Baby table from file complete in : 0.00000 sec
[+] seq value: 500000000000000    m value : 1000000000
[+] Search Range: 0x800000000000000000000000000000  to  0xffffffffffffffffffffffffffffff
                                                                 [+] k1: 0xe199457460ecec4f7bee5d197ec65f
PVK not found. 500.00000 Trillion scanned in 4.49 sec. New range [+] k1: 0xb01be1f673bcc76646b3e328f55378
PVK not found. 500.00000 Trillion scanned in 4.43 sec. New range [+] k1: 0xbba260e1fbf61c853a2e4b073efeb4
PVK not found. 500.00000 Trillion scanned in 4.52 sec. New range [+] k1: 0xa215357a619a1a210c306219e1a86e
PVK not found. 500.00000 Trillion scanned in 4.46 sec. New range [+] k1: 0xd50693c35208a07cd05b36cfb0a8a2
PVK not found. 500.00000 Trillion scanned in 4.51 sec. New range [+] k1: 0xd423f131b293593f130fbb169eeb48
PVK not found. 500.00000 Trillion scanned in 4.44 sec. New range [+] k1: 0xc76370873f34e006bbbae85e166eab
PVK not found. 500.00000 Trillion scanned in 4.78 sec. New range [+] k1: 0xb01a105a4dd48b5cdc494af16dc618
PVK not found. 500.00000 Trillion scanned in 4.72 sec. New range [+] k1: 0xfa3b11050d37e81c77d496256a7a4b
PVK not found. 500.00000 Trillion scanned in 4.70 sec. New range [+] k1: 0x81c1667af47679e78588d30a8d004b
PVK not found. 500.00000 Trillion scanned in 4.62 sec. New range [+] k1: 0xdaf3dbce0b3e9f8a907d04186875fc
PVK not found. 500.00000 Trillion scanned in 4.56 sec. New range [+] k1: 0xae3114f970986c87e9307f0ed95daa
PVK not found. 500.00000 Trillion scanned in 4.78 sec. New range [+] k1: 0xcf3469cdb06238b9d98f4d833b22a5
PVK not found. 500.00000 Trillion scanned in 4.98 sec. New range [+] k1: 0xdffcef85380fd649bbf55b09e6521c
PVK not found. 500.00000 Trillion scanned in 4.70 sec. New range [+] k1: 0xb13ab34b0bfa5273668e7725203772
PVK not found. 500.00000 Trillion scanned in 4.67 sec. New range [+] k1: 0xdb87af8a846e2b8cc6227a8528dfdf
PVK not found. 500.00000 Trillion scanned in 4.60 sec. New range [+] k1: 0xcc629816e977518b9c6e5b476052f8
PVK not found. 500.00000 Trillion scanned in 4.97 sec. New range [+] k1: 0xed55e1989580aeaf64b8d47be99b77
PVK not found. 500.00000 Trillion scanned in 4.62 sec. New range [+] k1: 0x8f373856662d2f6f4c31c0aed86548
PVK not found. 500.00000 Trillion scanned in 4.60 sec. New range [+] k1: 0xe654dd77a5a527e8f5fbe838f2f423


(base) C:\anaconda3>python bsgs_hybrid_dll_gmp.py -pfile Pub50.txt -b FULLbpfile.bin -bl Big5GB_dll_bloom.bin -n 8000000000 -rand1
[+] Starting Program : BSGS mode with hybrid algo using bloom dll
[+] Loading 34577 Public Keys to search
[+] Search Mode: Random Start then Fully sequential from it
[+] Reading bloom filter from file complete in : 2.58500 sec
[+] Reading Baby table from file complete in : 0.00000 sec
[+] seq value: 8000000000    m value : 1000000000
[+] Search Range: 0x1  to  0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364140
                                                              [+] k1: 0xb331769bc6a301dca4b1b9814f747b58a1b488964143c753c0de9acab31f45d6
PVK not found. 8.00000 Billion scanned in 3.34 sec. New range [+] k1: 0xb331769bc6a301dca4b1b9814f747b58a1b488964143c753c0de9acc8ff595d7
PVK not found. 8.00000 Billion scanned in 3.40 sec. New range [+] k1: 0xb331769bc6a301dca4b1b9814f747b58a1b488964143c753c0de9ace6ccbe5d8
PVK not found. 8.00000 Billion scanned in 3.29 sec. New range [+] k1: 0xb331769bc6a301dca4b1b9814f747b58a1b488964143c753c0de9ad049a235d9
PVK not found. 8.00000 Billion scanned in 3.10 sec. New range [+] k1: 0xb331769bc6a301dca4b1b9814f747b58a1b488964143c753c0de9ad2267885da
PVK not found. 8.00000 Billion scanned in 3.11 sec. New range [+] k1: 0xb331769bc6a301dca4b1b9814f747b58a1b488964143c753c0de9ad4034ed5db
PVK not found. 8.00000 Billion scanned in 3.06 sec. New range [+] k1: 0xb331769bc6a301dca4b1b9814f747b58a1b488964143c753c0de9ad5e02525dc
PVK not found. 8.00000 Billion scanned in 3.15 sec. New range [+] k1: 0xb331769bc6a301dca4b1b9814f747b58a1b488964143c753c0de9ad7bcfb75dd
PVK not found. 8.00000 Billion scanned in 3.43 sec. New range [+] k1: 0xb331769bc6a301dca4b1b9814f747b58a1b488964143c753c0de9ad999d1c5de
PVK not found. 8.00000 Billion scanned in 3.14 sec. New range [+] k1: 0xb331769bc6a301dca4b1b9814f747b58a1b488964143c753c0de9adb76a815df
PVK not found. 8.00000 Billion scanned in 3.35 sec. New range [+] k1: 0xb331769bc6a301dca4b1b9814f747b58a1b488964143c753c0de9add537e65e0
PVK not found. 8.00000 Billion scanned in 3.23 sec. New range [+] k1: 0xb331769bc6a301dca4b1b9814f747b58a1b488964143c753c0de9adf3054b5e1
PVK not found. 8.00000 Billion scanned in 3.07 sec. New range [+] k1: 0xb331769bc6a301dca4b1b9814f747b58a1b488964143c753c0de9ae10d2b05e2
PVK not found. 8.00000 Billion scanned in 3.06 sec. New range [+] k1: 0xb331769bc6a301dca4b1b9814f747b58a1b488964143c753c0de9ae2ea0155e3
PVK not found. 8.00000 Billion scanned in 3.01 sec. New range [+] k1: 0xb331769bc6a301dca4b1b9814f747b58a1b488964143c753c0de9ae4c6d7a5e4
PVK not found. 8.00000 Billion scanned in 3.13 sec. New range [+] k1: 0xb331769bc6a301dca4b1b9814f747b58a1b488964143c753c0de9ae6a3adf5e5
PVK not found. 8.00000 Billion scanned in 3.03 sec. New range [+] k1: 0xb331769bc6a301dca4b1b9814f747b58a1b488964143c753c0de9ae8808445e6
PVK not found. 8.00000 Billion scanned in 3.21 sec. New range [+] k1: 0xb331769bc6a301dca4b1b9814f747b58a1b488964143c753c0de9aea5d5a95e7
PVK not found. 8.00000 Billion scanned in 3.10 sec. New range [+] k1: 0xb331769bc6a301dca4b1b9814f747b58a1b488964143c753c0de9aec3a30e5e8
PVK not found. 8.00000 Billion scanned in 3.08 sec. New range [+] k1: 0xb331769bc6a301dca4b1b9814f747b58a1b488964143c753c0de9aee170735e9
```
**IceLand**
```
BTC:	bc1q39meky2mn5qjq704zz0nnkl0v7kj4uz6r529at
ETH:	0xa74fC23f07A33B90d6848dF0bb409bEA5Ac16b28
DOGE:	D5Wh5bQMc3XVGdLbjJbGjryjNom5tZY6dD
```
