# bsgs
Find PrivateKey of corresponding Pubkey(s) using BSGS algo.
Python3 implementation Using 1 thread. 

## v1_fastecdsa & v2_gmp & v3_gmp_bloom
README files moved to their corresponding folders

## LATEST Version : bsgs_dll_gmp
This script uses compiled library bloom.dll / bloom.so for Windows/Linux to handle the bloom part. The efficiency is increased in creating the bloomfilter file x10 times with overall Performance increase in Key Search is x3 times.

The main script to search for key using BSGS algo is bsgs_dll_gmp.py

## Usage
- ```python create_bPfile_mcpu.py 200000000 bPfile.bin 4```  _This uses 4 cpu to make bPfile with 200 million items._
- ```python bPfile_2_bloom_dll.py bpfile.bin bloomfile.bin```    _This converts that bPfile created earlier into a bloom file._
- ```python bsgs_dll_gmp.py -p 02CEB6CBBCDBDF5EF7150682150F4CE2C6F4807B349827DCDBDD1F2EFA885A2630 -b bPfile.bin -bl bloomfile.bin -n 50000000000000 -keyspace 800000000000000000000000000000:FFFFFFFFFFFFFFFFFFFFFFFFFFFFFF -rand```   _This is the main script to search for the pubkey using the files created earlier._

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


(base) C:\anaconda3>python bsgs_dll_gmp.py -p 02CEB6CBBCDBDF5EF7150682150F4CE2C6F4807B349827DCDBDD1F2EFA885A2630 -b FULLbpfile.bin -bl Big_dll_bloom.bin -n 50000000000000 -keyspace 800000000000000000000000000000:FFFFFFFFFFFFFFFFFFFFFFFFFFFFFF -rand
[+] Starting Program : BSGS mode
[+] Reading bloom filter from file complete in : 3.37594 sec
[+] Reading Baby table from file complete in : 0.00000 sec
[+] seq value: 50000000000000    m value : 400000000
[+] Search Range: 0x800000000000000000000000000000  to  0xffffffffffffffffffffffffffffff
                                                                [+] k1: 0xcf19d8c4c5a1677d75530779ed347d
PVK not found. 50.00000 Trillion scanned in 1.12 sec. New range [+] k1: 0x8a02f6b4a18150de5c0e56ae6b16d4
PVK not found. 50.00000 Trillion scanned in 1.12 sec. New range [+] k1: 0x8b562aa2d7cd32ac64fe32b2d50650
PVK not found. 50.00000 Trillion scanned in 1.09 sec. New range [+] k1: 0xe102340266bd7b218bf34c2478e22b
PVK not found. 50.00000 Trillion scanned in 1.11 sec. New range [+] k1: 0xaf8699585f72591e47de84be0e1b2b
PVK not found. 50.00000 Trillion scanned in 1.22 sec. New range [+] k1: 0x95cfd74eea4824767bf18925a7ff2a
PVK not found. 50.00000 Trillion scanned in 1.12 sec. New range [+] k1: 0x9b60432b7e36a9dc0324d3afdff9c5
PVK not found. 50.00000 Trillion scanned in 1.11 sec. New range [+] k1: 0x97208fbae40947da653dfe09150a46
PVK not found. 50.00000 Trillion scanned in 1.13 sec. New range [+] k1: 0xa1e84ac6576960fe4fe0dfb6b8b231
PVK not found. 50.00000 Trillion scanned in 1.11 sec. New range [+] k1: 0xcabd106790405e50fe65c8452c76cd
PVK not found. 50.00000 Trillion scanned in 1.12 sec. New range [+] k1: 0x878f16bf0635b40cb9c874fbdb0f8c
PVK not found. 50.00000 Trillion scanned in 1.12 sec. New range [+] k1: 0x9be8ab0fb87858b92a9164f0451bd2
PVK not found. 50.00000 Trillion scanned in 1.12 sec. New range [+] k1: 0x9172eb82394f79ef2004f662593b5a
PVK not found. 50.00000 Trillion scanned in 1.16 sec. New range [+] k1: 0xc05be46c45b7e30c17bc1988676fd1
PVK not found. 50.00000 Trillion scanned in 1.11 sec. New range [+] k1: 0xc7b16fec914fd586728865e82ea5ea
PVK not found. 50.00000 Trillion scanned in 1.19 sec. New range [+] k1: 0xf22810c55cb28eb8fe1e9030b87c20
PVK not found. 50.00000 Trillion scanned in 1.10 sec. New range [+] k1: 0xd6c7ea5976bfd753c6aaa77d4d4f65
PVK not found. 50.00000 Trillion scanned in 1.11 sec. New range [+] k1: 0xce8d663d92ef7caebe8bd17adccaa4
PVK not found. 50.00000 Trillion scanned in 1.10 sec. New range [+] k1: 0x9d4dff5a52ca5c80d35cf11107194a
PVK not found. 50.00000 Trillion scanned in 1.13 sec. New range [+] k1: 0x850b3530a5974465b70c913dcac736
PVK not found. 50.00000 Trillion scanned in 1.11 sec. New range [+] k1: 0xb6a0fcf9b135d3d5137e2eec167c19
PVK not found. 50.00000 Trillion scanned in 1.10 sec. New range [+] k1: 0xdcd8208aaf00bcffa8945100e54946
PVK not found. 50.00000 Trillion scanned in 1.11 sec. New range [+] k1: 0xf1ab525dac3c407f74c5a17e49d6b2
PVK not found. 50.00000 Trillion scanned in 1.13 sec. New range [+] k1: 0xc8be0bc701de5a7d31df2504d07487
PVK not found. 50.00000 Trillion scanned in 1.13 sec. New range [+] k1: 0xae7e2f2c6446d651945fbe4275af2d
PVK not found. 50.00000 Trillion scanned in 1.35 sec. New range [+] k1: 0xb8fec6b09253f556430cb52e45ca04
PVK not found. 50.00000 Trillion scanned in 1.28 sec. New range [+] k1: 0xdd5594d667fe1fddcbcb203905ba1d
PVK not found. 50.00000 Trillion scanned in 1.14 sec. New range [+] k1: 0x9cc421cc56f96b20179905b6acdbd9
PVK not found. 50.00000 Trillion scanned in 1.11 sec. New range [+] k1: 0xfb720dbd9304ff029a8f0484a74803
PVK not found. 50.00000 Trillion scanned in 1.13 sec. New range [+] k1: 0x9ab5596d82e6892936e25e387452e4
PVK not found. 50.00000 Trillion scanned in 1.16 sec. New range [+] k1: 0x912bc1dc651f7371b67058e29d1706
PVK not found. 50.00000 Trillion scanned in 1.11 sec. New range [+] k1: 0xd575ce2abf31927d73281c224973fb
PVK not found. 50.00000 Trillion scanned in 1.30 sec. New range [+] k1: 0x9d0180cded4d9763869a48e7986818
PVK not found. 50.00000 Trillion scanned in 1.12 sec. New range [+] k1: 0xd6fc3c39f2e39165b8faa68f6d745f
PVK not found. 50.00000 Trillion scanned in 1.11 sec. New range [+] k1: 0xe57cc28452d0ee6a6d1e07cc00e5ef
PVK not found. 50.00000 Trillion scanned in 1.10 sec. New range [+] k1: 0xf4ee45d516074c125d54329430c75f
PVK not found. 50.00000 Trillion scanned in 1.13 sec. New range [+] k1: 0xf44aeccb0678665f4511c2a19914f8
PVK not found. 50.00000 Trillion scanned in 1.12 sec. New range [+] k1: 0xb11b995ed3f2aa093dd9c5ebf77cd5
PVK not found. 50.00000 Trillion scanned in 1.12 sec. New range [+] k1: 0x985a24bfe64138bf0087257c753969
PVK not found. 50.00000 Trillion scanned in 1.13 sec. New range [+] k1: 0xfb16abbc61a6670909a87dd6618654
PVK not found. 50.00000 Trillion scanned in 1.12 sec. New range [+] k1: 0xbcd49f28dd709555609cf534691759
PVK not found. 50.00000 Trillion scanned in 1.13 sec. New range [+] k1: 0xe473cf6c5bec14be909bac9f01bb90
PVK not found. 50.00000 Trillion scanned in 1.10 sec. New range [+] k1: 0xdb861c3ae808d1bbf72662ec4c8c77
PVK not found. 50.00000 Trillion scanned in 1.11 sec. New range [+] k1: 0x8170e5143cc29fb6477a3dba9c4a18
PVK not found. 50.00000 Trillion scanned in 1.11 sec. New range [+] k1: 0xbb5cc51dda1ff60d29c5837711c437
PVK not found. 50.00000 Trillion scanned in 1.12 sec. New range [+] k1: 0xe9616063c922efe68dec472ac9773d
PVK not found. 50.00000 Trillion scanned in 1.11 sec. New range [+] k1: 0x950c910eb525db971b66ad0eeb3ffe
PVK not found. 50.00000 Trillion scanned in 1.18 sec. New range [+] k1: 0x8e643893c59e3cd511c7bdec3801b8
PVK not found. 50.00000 Trillion scanned in 1.16 sec. New range [+] k1: 0x96b32763021b1175f03c70bad24195
PVK not found. 50.00000 Trillion scanned in 1.15 sec. New range [+] k1: 0xa25568be5882cd09fde0f7671088e6
PVK not found. 50.00000 Trillion scanned in 1.20 sec. New range [+] k1: 0x9f03350841f5675673bb67ac0dc008
PVK not found. 50.00000 Trillion scanned in 1.32 sec. New range [+] k1: 0xd7f4bc716486077fe8efa67eacec1c
PVK not found. 50.00000 Trillion scanned in 1.20 sec. New range [+] k1: 0xe0fc6a50e134db7ddce5a367d87a72
PVK not found. 50.00000 Trillion scanned in 1.17 sec. New range [+] k1: 0xd9a531f547524bca03b506482322ab
PVK not found. 50.00000 Trillion scanned in 1.46 sec. New range [+] k1: 0xe8eec1ba37615f994db3d34ecddd9d

```
**IceLand**
```
BTC:	bc1q39meky2mn5qjq704zz0nnkl0v7kj4uz6r529at
ETH:	0xa74fC23f07A33B90d6848dF0bb409bEA5Ac16b28
DOGE:	D5Wh5bQMc3XVGdLbjJbGjryjNom5tZY6dD
```
