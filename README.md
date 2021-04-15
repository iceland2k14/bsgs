# bsgs
Find PrivateKey of corresponding Pubkey(s) using BSGS algo.
Python3 implementation Using 1 thread. 

# v1_fastecdsa
First time the program will create a table file in the same folder with name "baby_steps_table.txt" and will take some time.
Next time onwards this file will be directly used.

There are 2 scripts, bsgs_algo_modified.py for searching 1 pubkey or bsgs_algo_modified_multi.py for multiple pubkey from a text file.
This script require fastecdsa library and is slower than gmpy2 library.

# v2_gmp
Use bsgs_v4_gmp.py for 1 pubkey search. New Version is faster. Thanks to AlbertoBSD for a lot of discussion and help :) 
This script searches for 1 pubkey. 
You need to first, create a baby table file (bPfile.bin) using the provided script create_bPfile.py
Then use the script bsgs_v4_gmp.py for hunting the pubkey.
The constrained is RAM uasage here. It fills up very quickly with bigger bPfile for ex. 1 billion elements.

# v3_gmp_bloom
bsgs_v5_gmp.py script should bypass the RAM constraint by using bloom filter.
bPfile_2_bloom.py is used to convert the bPfile.bin created earlier into a bloomfilter file. this reduces the size.
Then bsgs_v5_gmp.py only uses this bloomfilter file to search for 1 pubkey. 
For ex. 400 million elements in the table only need 2GB bloomfilter file and therefore need only 2GB RAM.
You can prepare bigger table and hence bigger bloomfilter if the PC has more memory. It will be faster.

# bsgs_dll_gmp
This script uses compiled library bloom.dll / bloom.so for Windows/Linux to handle the bloom part. The efficiency is increased in creating the bloomfilter file x10 times.
Use the script bPfile_2_bloom_dll.py to create the bloomfile.
Then run main script to search for key using BSGS algo. It is bsgs_dll_gmp.py
Overall Performance increase in Key Search is x3 times.

# Run
```
(base) C:\anaconda3> python bsgs_algo_modified.py
Found the Baby Steps Table file: baby_steps_table.txt. Will be used directly
Checking 100000000000000 keys from 0x1
BSGS FOUND PrivateKey  : 0x2ec18388d544
Time Spent : 136.67 seconds


(base) C:\anaconda3>python bsgs_algo_modified_multi.py
Read 3 pubkeys from file
Found the Baby Steps Table file: baby_steps_table.txt. Will be used directly
Checking 100000000000000 keys from 0x1
BSGS FOUND PrivateKey  : 0x1d3
BSGS FOUND PrivateKey  : 0x17e2551e
BSGS FOUND PrivateKey  : 0x98fddfe4
Time Spent : 15.90 seconds. Speed 6269146771029.28 Keys/s
All PrivateKeys Found. Finished Searching


(base) C:\anaconda3>python bsgs_v4_gmp.py -p 02CEB6CBBCDBDF5EF7150682150F4CE2C6F4807B349827DCDBDD1F2EFA885A2630 -b FULLbpfile.bin -n 500000000000 -keyspace 800000000000000000000000000000:FFFFFFFFFFFFFFFFFFFFFFFFFFFFFF -rand
[+] Starting Program : BSGS mode
[+] Reading Baby table from file complete in : 0.75554 sec
[+] seq value: 500000000000    m value : 20000000
[+] Search Range: 0x800000000000000000000000000000  to  0xffffffffffffffffffffffffffffff
                                                                [+] k1: 0xae0ca830af9a9fac558c5c5ceef5a7
PVK not found. 500.00000 Billion scanned in 0.18 sec. New range [+] k1: 0xa3c7ed3d86bbe4181c3a37221a0da5
PVK not found. 500.00000 Billion scanned in 0.18 sec. New range [+] k1: 0xd4c90c752e4627f124b31bdb94c4f2
PVK not found. 500.00000 Billion scanned in 0.18 sec. New range [+] k1: 0xb6c900e87428a2a12cfb90b8484b96
PVK not found. 500.00000 Billion scanned in 0.18 sec. New range [+] k1: 0x9a28f237e7491f5fae336393ce0b94
PVK not found. 500.00000 Billion scanned in 0.18 sec. New range [+] k1: 0xbf1693d4d366372015ad7f12a0076b
PVK not found. 500.00000 Billion scanned in 0.18 sec. New range [+] k1: 0xc4cfaf5131dfe553dfbb2ee60078f8
PVK not found. 500.00000 Billion scanned in 0.18 sec. New range [+] k1: 0x9d37da4812bd1caf1c629cf77c1056
PVK not found. 500.00000 Billion scanned in 0.18 sec. New range [+] k1: 0xec2d260f7258b19b569cedad37a639
PVK not found. 500.00000 Billion scanned in 0.18 sec. New range [+] k1: 0xbdcc2a1a175d930227f3082ce3bafd
PVK not found. 500.00000 Billion scanned in 0.18 sec. New range [+] k1: 0x87347fd4e8ab0cf01a45c62e779cbd
PVK not found. 500.00000 Billion scanned in 0.22 sec. New range [+] k1: 0x9b5b02e9ee0563e12d7138f0cc8544
PVK not found. 500.00000 Billion scanned in 0.22 sec. New range [+] k1: 0x965261549b3f3ace040172405af75e
PVK not found. 500.00000 Billion scanned in 0.22 sec. New range [+] k1: 0xd84c7099e7ec03a27f23df9e0f2582
PVK not found. 500.00000 Billion scanned in 0.22 sec. New range [+] k1: 0xc3d2bfd31bd7aa525327bf74e4f6a0
PVK not found. 500.00000 Billion scanned in 0.18 sec. New range [+] k1: 0xbb2d00a87e49e7a91536771fed119a
PVK not found. 500.00000 Billion scanned in 0.18 sec. New range [+] k1: 0xbdf6b4a3ff2cbcffa33f87b104fb3c
PVK not found. 500.00000 Billion scanned in 0.18 sec. New range [+] k1: 0xdb7966c2f393ef3a13df463ed38ee6


(base) C:\anaconda3>python bsgs_v5_gmp.py -p 02CEB6CBBCDBDF5EF7150682150F4CE2C6F4807B349827DCDBDD1F2EFA885A2630 -b FULLbpfile.bin -bl Bigbloomfilter.bin -n 5000000000000 -keyspace 800000000000000000000000000000:FFFFFFFFFFFFFFFFFFFFFFFFFFFFFF -rand
[+] Starting Program : BSGS mode
[+] Reading bloom filter from file complete in : 1.89686 sec
[+] Reading Baby table from file complete in : 0.00000 sec
[+] seq value: 5000000000000    m value : 400000000
[+] Search Range: 0x800000000000000000000000000000  to  0xffffffffffffffffffffffffffffff
                                                               [+] k1: 0xf86438d726027e9ce24b14afebef1d
PVK not found. 5.00000 Trillion scanned in 0.31 sec. New range [+] k1: 0xc6091f4cbc596952abdd10a4e010d7
PVK not found. 5.00000 Trillion scanned in 0.38 sec. New range [+] k1: 0xed3526a5934b5a3609ee9f8a439f89
PVK not found. 5.00000 Trillion scanned in 0.29 sec. New range [+] k1: 0xb46916db3856d7ff5160f2a4a8623b
PVK not found. 5.00000 Trillion scanned in 0.30 sec. New range [+] k1: 0x9605fe55f55b0583b330980a9b17d8
PVK not found. 5.00000 Trillion scanned in 0.30 sec. New range [+] k1: 0xfb6f2853eab745b3a3983fed06bded
PVK not found. 5.00000 Trillion scanned in 0.29 sec. New range [+] k1: 0x89f6195bbb33bdc7676862ab41836c
PVK not found. 5.00000 Trillion scanned in 0.29 sec. New range [+] k1: 0xcbb62284cd23839a4983c3cd2be5ca
PVK not found. 5.00000 Trillion scanned in 0.38 sec. New range [+] k1: 0xb9c40cfa21e4658a6e764cee4c0dbf
PVK not found. 5.00000 Trillion scanned in 0.39 sec. New range [+] k1: 0xe6e41a71365becee1eb4589215b842
PVK not found. 5.00000 Trillion scanned in 0.32 sec. New range [+] k1: 0xd883d99e66de8fd9b9b4c4a4ba2fb3
PVK not found. 5.00000 Trillion scanned in 0.30 sec. New range [+] k1: 0xe90449e4ac03035405f1c52c91c20a
PVK not found. 5.00000 Trillion scanned in 0.38 sec. New range [+] k1: 0xd058c0fc79ad35100da6abd29c0118
PVK not found. 5.00000 Trillion scanned in 0.32 sec. New range [+] k1: 0xb440a8b62fd6936e4fcd2b385f1691
PVK not found. 5.00000 Trillion scanned in 0.30 sec. New range [+] k1: 0xcb4f21d3d0fbcf4a600db1e619b4fd
PVK not found. 5.00000 Trillion scanned in 0.29 sec. New range [+] k1: 0xf026cd847a65406927b0ac51cf0cb5


(base) C:\anaconda3>python bsgs_hybrid_gmp.py -pfile Pub50.txt -b FULLbpfile.bin -bl Bigbloomfilter.bin -n 8000000000 -rand
[+] Starting Program : BSGS mode with hybrid algo using bloom
[+] Loading 34577 Public Keys to search
[+] Reading bloom filter from file complete in : 1.98043 sec
[+] Reading Baby table from file complete in : 0.00000 sec
[+] seq value: 8000000000    m value : 400000000
[+] Search Range: 0x1  to  0x7fffffffffffffffffffffffffffffff5d576e7357a4501ddfe92f46681b20a0
                                                               [+] k1: 0x7b6d1063194855450b1027d1e70e3a027d17c12294f8ca5621936db1a3da0dc6
PVK not found. 8.00000 Billion scanned in 17.72 sec. New range [+] k1: 0x395277ea5ee6c7d81721af94e756abd496f1cf06c511dd3c24e9eb1bd3c02720
PVK not found. 8.00000 Billion scanned in 17.76 sec. New range [+] k1: 0xa807af4cb93b49b9b410b3b9514fe13e55d389d86568dbbc32021d674fbd1e9
PVK not found. 8.00000 Billion scanned in 22.56 sec. New range [+] k1: 0x72b53d73f191f44aa86bbe8e109e70f74d7c90a1b103db74e803c0155275853f
PVK not found. 8.00000 Billion scanned in 21.45 sec. New range [+] k1: 0x47467eadacb90710d8627287c090c598c95fa6e50d278a74d4407ae9095a093a
PVK not found. 8.00000 Billion scanned in 20.69 sec. New range [+] k1: 0x69ce4c10554cae4b11ce9efad3f846b86deaf9091df56e7964fff6d20839a0b7
PVK not found. 8.00000 Billion scanned in 21.07 sec. New range [+] k1: 0x557cebfbd460b29b6d6d72e5ebf62b92029c5a23905e8fdc25e8dcac3beffa20
PVK not found. 8.00000 Billion scanned in 20.93 sec. New range [+] k1: 0x6d679ec05c9cba280ce37d57621904ee3c40b13b9db572cae31bd30f93cec448
PVK not found. 8.00000 Billion scanned in 21.48 sec. New range [+] k1: 0x96d8875dd156f5ca3479182d469d1a473570c0afa1d513647a23bf36685e281
PVK not found. 8.00000 Billion scanned in 23.05 sec. New range [+] k1: 0x4ff7418bbfc0997120c35832a359dac4f4ceb67ccbcee063dffa158dcede3bf9
PVK not found. 8.00000 Billion scanned in 20.45 sec. New range [+] k1: 0x757fe61f758d4120be78a0e9d93e8378cd2b80d010a6415a41e0791017ae898a


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
**IceLand **
```
BTC:	bc1q39meky2mn5qjq704zz0nnkl0v7kj4uz6r529at
ETH:	0xa74fC23f07A33B90d6848dF0bb409bEA5Ac16b28
DOGE:	D5Wh5bQMc3XVGdLbjJbGjryjNom5tZY6dD
```
