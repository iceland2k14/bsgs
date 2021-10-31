## v5_dll_secp256k1_bloom
This script uses compiled library bloom_batch.dll / bloom_batch.so for Windows/Linux to handle the bloom part. The EC math part has been selected from secp256k1 compiled library. The efficiency is increased in creating the bpfile, bloomfilter file and overall Performance increase in Key Search.

The main script to search 1 public key using BSGS algo is bsgs_dll_secp256k1.py

Another script _bsgs_hybrid_dll_secp256k1.py_ has been include to search multiple publickeys all Together (not 1 by 1). Here the script can search millions of pubkey at once but the speed reduces quickly. Although it is still faster than searching the address or HASH160.

## Usage
- ```python create_bPfile_mcpu2.py 200000000 bPfile.bin 4```  _This uses 4 cpu to make bPfile with 200 million items._
- ```python bPfile_2_bloom_dll_batch.py bpfile.bin bloomfile.bin```    _This converts that bPfile created earlier into a bloom file._
- ```python bsgs_dll_secp256k1.py -p 02CEB6CBBCDBDF5EF7150682150F4CE2C6F4807B349827DCDBDD1F2EFA885A2630 -b bPfile.bin -bl bloomfile.bin -n 50000000000000 -keyspace 800000000000000000000000000000:FFFFFFFFFFFFFFFFFFFFFFFFFFFFFF -rand```   _This is the main script to search for 1 pubkey using the files created earlier._
- ```python bsgs_hybrid_dll_secp256k1.py -pfile Pub50.txt -b FULLbpfile.bin -bl Big5GB_dll_bloom.bin -n 8000000000 -rand1```   _This is the main script to search for multi pubkey using the files created earlier._

***Note: Think about How much RAM your system has free which you are going to allow to use in this script.
For Example 1 billion items will require 5GB bloom file and therefore 5GB for running the final script. So plan accordingly during creation of bPfile and bloomfile.***
|    RAM     | bpfile elements | bpfile size | bloom size  |
| ---------- | --------------- | ----------- | ----------- |
|   8 GB     | 1000000000      |   32 GB     |   5.02  GB  |
|  32 GB     | 5000000000      |   160 GB    |   25.11 GB  |
|  128 GB    | 22000000000     |   704 GB    |   110.47 GB |
|  500 GB    | 90000000000     |   2.9 TB    |   451.92 GB |

# Run
```
(base) C:\anaconda3>python create_bPfile_mcpu2.py 37000000 yybPfile.bin 4
[+] Program Running please wait...
[+] Each chunk size : 10000000
[+] Created Total 4 Chunks ...
[+] Working on Chunk 1 ...
[+] Working on Chunk 2 ...
[+] Working on Chunk 3 ...
[+] Working on Chunk 4 ...
[+] File created successfully
[-] Completed in 37.92 sec


(base) C:\anaconda3>python bPfile_2_bloom_dll_batch.py yybpfile.bin yy_bloom.bin
bloom bits  : 1595912224    size [190 MB]
bloom hashes: 30
[+] Initializing the bloom filters to null
[+] Reading Baby table from file  37000000  elements
[+] Created 37 Chunks ...
[+] Inserting baby table elements in bloom filter: Updating bloom in chunks
[+] Freeing some memory
[+] Saving bloom filter to file
[-] Completed in 87.70 sec


(base) C:\anaconda3>python bsgs_dll_secp256k1.py -p 02CEB6CBBCDBDF5EF7150682150F4CE2C6F4807B349827DCDBDD1F2EFA885A2630 -b 2B_bPfile.bin -bl 2B_bloom.bin -n 500000000000000 -keyspace 800000000000000000000000000000:FFFFFFFFFFFFFFFFFFFFFFFFFFFFFF -rand
[+] Starting Program : BSGS mode     Version [ 26062021 ]
[+] Search Started for the Public key:  04ceb6cbbcdbdf5ef7150682150f4ce2c6f4807b349827dcdbdd1f2efa885a26302b195386bea3f5f002dc033b92cfc2c9e71b586302b09cfe535e1ff290b1b5ac
[+] Search Mode: Random Start after every n sequential key search
[+] Reading bloom filter from file complete in : 4.62167 sec
[+] Reading Baby table from file complete in : 0.15386 sec
[+] seq value: 500000000000000    m value : 2000000000
[+] Search Range: 0x800000000000000000000000000000  to  0xffffffffffffffffffffffffffffff
                                                                 [+] k1: 0xe818296b43419d02cb1011a0cfffc8
PVK not found. 500.00000 Trillion scanned in 1.13 sec. New range [+] k1: 0xfe50fb43a9c13170d122298cd52d5b
PVK not found. 500.00000 Trillion scanned in 1.09 sec. New range [+] k1: 0xc193c4203e042a035c94d605c810ea
PVK not found. 500.00000 Trillion scanned in 1.06 sec. New range [+] k1: 0x8ae6fdd2f6216ac467b29bf0ea32a0
PVK not found. 500.00000 Trillion scanned in 1.18 sec. New range [+] k1: 0xcc01ec9a87ebcb1a6ea6d7c5ea9457
PVK not found. 500.00000 Trillion scanned in 1.10 sec. New range [+] k1: 0xa28cfb461eb304f25b70d7d52a3a4f
PVK not found. 500.00000 Trillion scanned in 1.12 sec. New range [+] k1: 0xb6de8f8f150f2f8ef42433ea19b29e
PVK not found. 500.00000 Trillion scanned in 1.06 sec. New range [+] k1: 0x9e54e29a657032dfccebed65435b95
PVK not found. 500.00000 Trillion scanned in 1.05 sec. New range [+] k1: 0xfc7c87feb6b041e6d6aef5562b6215
PVK not found. 500.00000 Trillion scanned in 1.09 sec. New range [+] k1: 0xcd29d8289d4bc1fed2ab3249fc5e10
PVK not found. 500.00000 Trillion scanned in 1.12 sec. New range [+] k1: 0xbc84c7fbfd6f036e155926d995d82a
PVK not found. 500.00000 Trillion scanned in 1.04 sec. New range [+] k1: 0xdd6308f834e554fcb36ebeddf6f6d1
PVK not found. 500.00000 Trillion scanned in 1.12 sec. New range [+] k1: 0xeca8338b51daa0c2432588e90cfb0e
PVK not found. 500.00000 Trillion scanned in 1.07 sec. New range [+] k1: 0xa2dc0ed8ec5530e8eba6b4929dfd7e
PVK not found. 500.00000 Trillion scanned in 1.05 sec. New range [+] k1: 0x8208a669078dcff13461c0a3a6b21c
PVK not found. 500.00000 Trillion scanned in 1.07 sec. New range [+] k1: 0x83c83e764d6a4c9a1d1cc31eba3894
PVK not found. 500.00000 Trillion scanned in 1.04 sec. New range [+] k1: 0x804f1c832cb1a10cca1734738a1f3d
PVK not found. 500.00000 Trillion scanned in 1.03 sec. New range [+] k1: 0xd0b41062487e7f0abf649741e9a3d8
PVK not found. 500.00000 Trillion scanned in 1.02 sec. New range [+] k1: 0xa38b6c39ed42d7c3cb3de5ac499dd0
PVK not found. 500.00000 Trillion scanned in 1.05 sec. New range [+] k1: 0xc2414d07978404720ee9ba609fe942
PVK not found. 500.00000 Trillion scanned in 1.03 sec. New range [+] k1: 0xa2931edc917735361b56a2f0e20a56
PVK not found. 500.00000 Trillion scanned in 1.04 sec. New range [+] k1: 0xb67a2ffd78cdb1d398562e47222b52
PVK not found. 500.00000 Trillion scanned in 1.07 sec. New range [+] k1: 0xdf594ef55a11aa7b6eacc39c634885
PVK not found. 500.00000 Trillion scanned in 1.03 sec. New range [+] k1: 0xcb9764b34b23fda417135a12fdbb48
PVK not found. 500.00000 Trillion scanned in 1.03 sec. New range [+] k1: 0xa5b03e9ee84967da7fd47437cb7703
PVK not found. 500.00000 Trillion scanned in 1.03 sec. New range [+] k1: 0xba2708befe847c9ca40af41eb36328
PVK not found. 500.00000 Trillion scanned in 1.02 sec. New range [+] k1: 0xabc6e64473de5ffb5a62f32c98b7ad


(base) C:\anaconda3>python bsgs_hybrid_dll_secp256k1.py -pfile Pub50.txt -b FULLbpfile.bin -bl 2B_bloom.bin -n 8000000000 -rand1
[+] Starting Program : BSGS mode with hybrid algo using bloom dll and secp256k1 dll     Version [ 26062021 ]
[+] Loading 34577 Public Keys to search
[+] Search Mode: Random Start then Fully sequential from it
[+] Reading bloom filter from file complete in : 4.81413 sec
[+] Reading Baby table from file complete in : 0.09243 sec
[+] seq value: 8000000000    m value : 2000000000
[+] Search Range: 0x1  to  0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364140
                                                              [+] k1: 0x4a6808e02a457927edf2ec8c05afb5e4b112dee0e3be496e86801579b3635208
PVK not found. 8.00000 Billion scanned in 1.35 sec. New range [+] k1: 0x4a6808e02a457927edf2ec8c05afb5e4b112dee0e3be496e8680157b9039a209
PVK not found. 8.00000 Billion scanned in 1.31 sec. New range [+] k1: 0x4a6808e02a457927edf2ec8c05afb5e4b112dee0e3be496e8680157d6d0ff20a
PVK not found. 8.00000 Billion scanned in 1.40 sec. New range [+] k1: 0x4a6808e02a457927edf2ec8c05afb5e4b112dee0e3be496e8680157f49e6420b
PVK not found. 8.00000 Billion scanned in 1.32 sec. New range [+] k1: 0x4a6808e02a457927edf2ec8c05afb5e4b112dee0e3be496e8680158126bc920c
PVK not found. 8.00000 Billion scanned in 1.30 sec. New range [+] k1: 0x4a6808e02a457927edf2ec8c05afb5e4b112dee0e3be496e868015830392e20d
PVK not found. 8.00000 Billion scanned in 1.34 sec. New range [+] k1: 0x4a6808e02a457927edf2ec8c05afb5e4b112dee0e3be496e86801584e069320e
PVK not found. 8.00000 Billion scanned in 1.31 sec. New range [+] k1: 0x4a6808e02a457927edf2ec8c05afb5e4b112dee0e3be496e86801586bd3f820f
PVK not found. 8.00000 Billion scanned in 1.31 sec. New range [+] k1: 0x4a6808e02a457927edf2ec8c05afb5e4b112dee0e3be496e868015889a15d210
PVK not found. 8.00000 Billion scanned in 1.32 sec. New range [+] k1: 0x4a6808e02a457927edf2ec8c05afb5e4b112dee0e3be496e8680158a76ec2211
PVK not found. 8.00000 Billion scanned in 1.33 sec. New range [+] k1: 0x4a6808e02a457927edf2ec8c05afb5e4b112dee0e3be496e8680158c53c27212
PVK not found. 8.00000 Billion scanned in 1.32 sec. New range [+] k1: 0x4a6808e02a457927edf2ec8c05afb5e4b112dee0e3be496e8680158e3098c213
PVK not found. 8.00000 Billion scanned in 1.32 sec. New range [+] k1: 0x4a6808e02a457927edf2ec8c05afb5e4b112dee0e3be496e868015900d6f1214
PVK not found. 8.00000 Billion scanned in 1.36 sec. New range [+] k1: 0x4a6808e02a457927edf2ec8c05afb5e4b112dee0e3be496e86801591ea456215
PVK not found. 8.00000 Billion scanned in 1.31 sec. New range [+] k1: 0x4a6808e02a457927edf2ec8c05afb5e4b112dee0e3be496e86801593c71bb216
PVK not found. 8.00000 Billion scanned in 1.31 sec. New range [+] k1: 0x4a6808e02a457927edf2ec8c05afb5e4b112dee0e3be496e86801595a3f20217
PVK not found. 8.00000 Billion scanned in 1.33 sec. New range [+] k1: 0x4a6808e02a457927edf2ec8c05afb5e4b112dee0e3be496e8680159780c85218
PVK not found. 8.00000 Billion scanned in 1.30 sec. New range [+] k1: 0x4a6808e02a457927edf2ec8c05afb5e4b112dee0e3be496e868015995d9ea219
PVK not found. 8.00000 Billion scanned in 1.32 sec. New range [+] k1: 0x4a6808e02a457927edf2ec8c05afb5e4b112dee0e3be496e8680159b3a74f21a
PVK not found. 8.00000 Billion scanned in 1.32 sec. New range [+] k1: 0x4a6808e02a457927edf2ec8c05afb5e4b112dee0e3be496e8680159d174b421b
```
