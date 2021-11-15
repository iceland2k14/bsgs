# bsgs
Find PrivateKey of corresponding Pubkey(s) using BSGS algo.
Python3 implementation. 

### v1_fastecdsa & v2_gmp & v3_gmp_bloom & v4_dll_gmp_bloom & v5_secp256k1_bloom_dll
README files moved to their corresponding folders

## LATEST Version : v6_dll_bsgs
This script uses compiled library BSGS.dll / BSGS.so for Windows/Linux to handle the bloom part. The EC math part has been selected from secp256k1 compiled library. The efficiency is increased in creating the bpfile, bloomfilter file and overall Performance increase in Key Search.

## Usage
- ```python bsgs_create_bpfile_bloomfile.py 3000000000 bpfile.bin bloomfile.bin 4```  _This uses 4 cpu to make bPfile and bloomfile with 3 billion items._
- ```python bsgs_dll_secp256k1.py -p 02CEB6CBBCDBDF5EF7150682150F4CE2C6F4807B349827DCDBDD1F2EFA885A2630 -b bPfile.bin -bl bloomfile.bin -n 50000000000000 -keyspace 800000000000000000000000000000:FFFFFFFFFFFFFFFFFFFFFFFFFFFFFF -rand```   _This is the main script to search for 1 pubkey using the files created earlier._
- ```python bsgs_hybrid_dll_secp256k1.py -pfile Pub50.txt -b FULLbpfile.bin -bl Big5GB_dll_bloom.bin -n 8000000000 -rand1```   _This is the main script to search for multi pubkey using the files created earlier._

***Note: Think about How much RAM your system has free which you are going to allow to use in this script.
For Example 1 billion items will require 5GB bloom file and therefore 5GB for running the final script. So plan accordingly during creation of bPfile and bloomfile.***
|    RAM     | total elements  | bloom size  |
| ---------- | --------------- | ----------- |
|   8 GB     | 1000000000      |   5.02  GB  |
|  32 GB     | 5000000000      |   25.11 GB  |
|  128 GB    | 22000000000     |   110.47 GB |
|  500 GB    | 90000000000     |   451.92 GB |

# Run
```
(base) C:\anaconda3>python bsgs_create_bpfile_bloomfile.py 3000000000 bpfile.bin bloomfile.bin 4

[+] Program Running please wait...
[+] Number of items required for Final Script : [bp : 54773] [bloom : 3000000000]
[+] Output Size of the files : [bp : 1752736 Bytes] [bloom : 16174786012 Bytes]
[+] Creating bpfile in range 1 to 54773
[+] File : bpfile.bin created successfully in 0.13 sec

[+] Starting bloom file creation ... with False Positive probability : 1e-09
[+] bloom bits  : 129398288096    size [15425 MB]
[+] bloom hashes: 30
[+] Initializing the bloom filters to null
[+] Number of CPU thread: 4
[+] Thread  0: 0x0000000000000001 -> 0x000000002CB41780
[+] Thread  1: 0x000000002CB41781 -> 0x0000000059682F00
[+] Thread  2: 0x0000000059682F01 -> 0x00000000861C4680
[+] Thread  3: 0x00000000861C4681 -> 0x00000000B2D05E00
[+] Saving bloom filter to File
[+] File : bloomfile.bin created successfully in 7908.88 sec
[+] Program Finished


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

```
# GPU Run
```
(base) C:\anaconda3\v7_gpu_trial>python bsgs_GPU.py -pubkey 02CEB6CBBCDBDF5EF7150682150F4CE2C6F4807B349827DCDBDD1F2EFA885A2630 -n 1000000000000000000 -d 0 -t 256 -b 20 -p 512 -bp 30000000 -keyspace 800000000000000000000000000000:ffffffffffffffffffffffffffffff -rand

[+] Starting Program.... Please Wait !
[+] Search Mode: Random Start after every n sequential key search
[2021-11-15.20:45:50] [Info] Starting at : 80810F961749F8823F4871B47E7DEB (120 bit)
[2021-11-15.20:45:50] [Info] Ending at   : 80810F961749F8901FFF255BE27DEB (120 bit)
[2021-11-15.20:45:50] [Info] Initializing Quadro K2100M
[2021-11-15.20:52:04] [Info] Allocating bloom filter (1024.0MB)
[DEV: Quadro K2100M    1785/2048MB] [K: 80810F961749F883C214195EBE7DEB (120 bit), C: 10.887326 %] [I: E980A4 (24 bit), 1] [T: 30000000] [S: 613.62 TK/s] [213,437,644,800,000,000 (33 bit)] [00:05:26]
```

**IceLand**
```
BTC:	bc1q39meky2mn5qjq704zz0nnkl0v7kj4uz6r529at
ETH:	0xa74fC23f07A33B90d6848dF0bb409bEA5Ac16b28
DOGE:	D5Wh5bQMc3XVGdLbjJbGjryjNom5tZY6dD
```
