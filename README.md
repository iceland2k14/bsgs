# bsgs
Find PrivateKey of corresponding Pubkey(s) using BSGS algo.
Python3 implementation. 

### v1_fastecdsa & v2_gmp & v3_gmp_bloom & v4_dll_gmp_bloom & v5_secp256k1_bloom_dll
README files moved to their corresponding folders

### LATEST Version : v6_dll_bsgs and v7_gpu_trial
This script uses compiled library BSGS.dll / BSGS.so for Windows/Linux to handle the bloom part. The EC math part has been selected from secp256k1 compiled library. The efficiency is increased in creating the bpfile, bloomfilter file and overall Performance increase in Key Search.

## Usage
- ```python bsgs_create_bpfile_bloomfile.py 3000000000 bpfile.bin bloomfile.bin 4```  _This uses 4 cpu to make bPfile and bloomfile with 3 billion items._
- ```python bsgs_dll_search.py -keyspace 800000000000000000000000000000:FFFFFFFFFFFFFFFFFFFFFFFFFFFFFF -b bpfile.bin -bl bloomfile.bin -p 02CEB6CBBCDBDF5EF7150682150F4CE2C6F4807B349827DCDBDD1F2EFA885A2630 -rand```   _This is the main script to search for 1 pubkey using the files created earlier._
- ```python bsgs_dll_search.py -pfile Pub50.txt -b bpfile.bin -bl bloomfile.bin -rand1```   _This is the main script to search for multi pubkey using the files created earlier._
- Option ```rand``` and ```rand1``` is personal choice. rand changes the base key randomly after each n items while rand1 does it only first time.

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


(base) C:\anaconda3>python bsgs_dll_search.py -b bpfile.bin -bl bloomfile.bin -rand1 -p 02CEB6CBBCDBDF5EF7150682150F4CE2C6F4807B349827DCDBDD1F2EFA885A2630 -keyspace 800000000000000000000000000000:FFFFFFFFFFFFFFFFFFFFFFFFFFFFFF

[+] Starting Program : BSGS mode     Version [ 02012022 ]
[+] Search Started for the Public key:  04ceb6cbbcdbdf5ef7150682150f4ce2c6f4807b349827dcdbdd1f2efa885a26302b195386bea3f5f002dc033b92cfc2c9e71b586302b09cfe535e1ff290b1b5ac
[+] Search Mode: Random Start then Fully sequential from it
[+] Reading bloom filter from file complete in : 200.29923 sec
[+] Reading Baby table from file complete in : 0.05340 sec
[+] seq value: 15000000000000000    m value : 3000000000
[+] Search Range: 0x800000000000000000000000000000  to  0xffffffffffffffffffffffffffffff
                                                                 [+] k1: 0xf721b046614f9c7d9a894624176839
PVK not found. 15.00000 PetaKeys scanned in 12.19 sec. New range [+] k1: 0xf721b046614f9c7dcfd3b1cbb8e83a
PVK not found. 15.00000 PetaKeys scanned in 11.56 sec. New range [+] k1: 0xf721b046614f9c7e051e1d735a683b
PVK not found. 15.00000 PetaKeys scanned in 11.41 sec. New range [+] k1: 0xf721b046614f9c7e3a68891afbe83c
PVK not found. 15.00000 PetaKeys scanned in 11.49 sec. New range [+] k1: 0xf721b046614f9c7e6fb2f4c29d683d
PVK not found. 15.00000 PetaKeys scanned in 11.60 sec. New range [+] k1: 0xf721b046614f9c7ea4fd606a3ee83e
PVK not found. 15.00000 PetaKeys scanned in 11.47 sec. New range [+] k1: 0xf721b046614f9c7eda47cc11e0683f
PVK not found. 15.00000 PetaKeys scanned in 11.68 sec. New range [+] k1: 0xf721b046614f9c7f0f9237b981e840
PVK not found. 15.00000 PetaKeys scanned in 11.65 sec. New range [+] k1: 0xf721b046614f9c7f44dca361236841
PVK not found. 15.00000 PetaKeys scanned in 11.58 sec. New range [+] k1: 0xf721b046614f9c7f7a270f08c4e842
PVK not found. 15.00000 PetaKeys scanned in 12.92 sec. New range [+] k1: 0xf721b046614f9c7faf717ab0666843
PVK not found. 15.00000 PetaKeys scanned in 12.09 sec. New range [+] k1: 0xf721b046614f9c7fe4bbe65807e844
PVK not found. 15.00000 PetaKeys scanned in 11.94 sec. New range [+] k1: 0xf721b046614f9c801a0651ffa96845
PVK not found. 15.00000 PetaKeys scanned in 12.44 sec. New range [+] k1: 0xf721b046614f9c804f50bda74ae846
PVK not found. 15.00000 PetaKeys scanned in 12.29 sec. New range [+] k1: 0xf721b046614f9c80849b294eec6847
PVK not found. 15.00000 PetaKeys scanned in 12.41 sec. New range [+] k1: 0xf721b046614f9c80b9e594f68de848
PVK not found. 15.00000 PetaKeys scanned in 12.37 sec. New range [+] k1: 0xf721b046614f9c80ef30009e2f6849
PVK not found. 15.00000 PetaKeys scanned in 12.43 sec. New range [+] k1: 0xf721b046614f9c81247a6c45d0e84a
PVK not found. 15.00000 PetaKeys scanned in 12.74 sec. New range [+] k1: 0xf721b046614f9c8159c4d7ed72684b

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
DOGE:	D5Wh5bQMc3XVGdLbjJbGjryjNom5tZY6dD
```
