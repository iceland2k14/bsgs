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

# bsgs_v5_gmp
This script should bypass the RAM constraint by using bloom filter.
bPfile_2_bloom.py is used to convert the bPfile.bin created earlier into a bloomfilter file. this reduces the size.
Then bsgs_v5_gmp.py only uses this bloomfilter file to search for 1 pubkey. 
For ex. 400 million elements in the table only need 2GB bloomfilter file and therefore need only 2GB RAM.
You can prepare bigger table and hence bigger bloomfilter if the PC has more memory. It will be faster.

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


(base) C:\anaconda3>python bsgs_v5_gmp.py -p 02CEB6CBBCDBDF5EF7150682150F4CE2C6F4807B349827DCDBDD1F2EFA885A2630 -bl Bigbloomfilter.bin -n 5000000000000 -keyspace 800000000000000000000000000000:FFFFFFFFFFFFFFFFFFFFFFFFFFFFFF -rand
[+] Starting Program : BSGS mode
[+] Reading bloom filter from file complete in : 2.05280 sec
[+] seq value: 5000000000000    m value : 400000000
[+] Search Range: 0x800000000000000000000000000000  to  0xffffffffffffffffffffffffffffff
                                                               [+] k1: 0xb58ff37d5f981645cd6e56b185cb30
PVK not found. 5.00000 Trillion scanned in 0.35 sec. New range [+] k1: 0xa3f2d31a09e68bc678645fdcc5a14e
PVK not found. 5.00000 Trillion scanned in 0.33 sec. New range [+] k1: 0xc395ee9a85466273a4ca114fb64965
PVK not found. 5.00000 Trillion scanned in 0.32 sec. New range [+] k1: 0x98052c0921e0b10ccee4ab83f63cbe
PVK not found. 5.00000 Trillion scanned in 0.32 sec. New range [+] k1: 0xc83f634ef6ca0917c1e9d40e973ac2
PVK not found. 5.00000 Trillion scanned in 0.36 sec. New range [+] k1: 0xbece9fdf4bcec3fdece41d3c2bc28e
PVK not found. 5.00000 Trillion scanned in 0.35 sec. New range [+] k1: 0x93e086ffea6fc89958b5031098d539
PVK not found. 5.00000 Trillion scanned in 0.31 sec. New range [+] k1: 0xa27d8617a10eeb649e89cff01740a1
PVK not found. 5.00000 Trillion scanned in 0.31 sec. New range [+] k1: 0x92134abb1bf8a98c7f84550705d7a2
PVK not found. 5.00000 Trillion scanned in 0.32 sec. New range [+] k1: 0x995c8f130ec7f7b506b0c4086502f3
PVK not found. 5.00000 Trillion scanned in 0.42 sec. New range [+] k1: 0xe6d830742b3f29265f670d6223adb0
PVK not found. 5.00000 Trillion scanned in 0.35 sec. New range [+] k1: 0xc64ce1429698200cdd9187a1143b13
PVK not found. 5.00000 Trillion scanned in 0.31 sec. New range [+] k1: 0x854d4562eb2a355a9eaa8421f8b15d
PVK not found. 5.00000 Trillion scanned in 0.35 sec. New range [+] k1: 0x996525dd050224464fa4be25180203
PVK not found. 5.00000 Trillion scanned in 0.31 sec. New range [+] k1: 0xa99ca78d22afbc305f2199d4e27ccf
PVK not found. 5.00000 Trillion scanned in 0.37 sec. New range [+] k1: 0xbd89677b1ab835c496beb019fc0230
PVK not found. 5.00000 Trillion scanned in 0.34 sec. New range [+] k1: 0xe4d3dcd5db60d837f26a67922e8e4d
PVK not found. 5.00000 Trillion scanned in 0.34 sec. New range [+] k1: 0xbdfe968df6c7b63ccc254060284472
PVK not found. 5.00000 Trillion scanned in 0.36 sec. New range [+] k1: 0xa5a8aaf4e5741226b6c03d62d9118b
PVK not found. 5.00000 Trillion scanned in 0.33 sec. New range [+] k1: 0x9e8a4f03cd05e8e47695dea01a0c18
PVK not found. 5.00000 Trillion scanned in 0.38 sec. New range [+] k1: 0xdc651933ff2703b24c0fb80044e0a5
PVK not found. 5.00000 Trillion scanned in 0.31 sec. New range [+] k1: 0xb432ca6d398781dedf0adb4da7777d
PVK not found. 5.00000 Trillion scanned in 0.37 sec. New range [+] k1: 0xa15780af9e12f5567d6f57a13286de
PVK not found. 5.00000 Trillion scanned in 0.32 sec. New range [+] k1: 0xfda61a4030417cd17986d72cd2961f
PVK not found. 5.00000 Trillion scanned in 0.32 sec. New range [+] k1: 0xb65c49aa73cc80e41700ab21d19ff7

```
**IceLand **
```
BTC:	bc1q39meky2mn5qjq704zz0nnkl0v7kj4uz6r529at
ETH:	0xa74fC23f07A33B90d6848dF0bb409bEA5Ac16b28
DOGE:	D5Wh5bQMc3XVGdLbjJbGjryjNom5tZY6dD
```
