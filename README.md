# bsgs
Find PrivateKey of corresponding Pubkey(s) using BSGS algo.
Python3 implementation Using 1 thread. 

First time the program will create a table file in the same folder with name "baby_steps_table.txt" and will take some time.
Next time onwards this file will be directly used.

Use bsgs_v4_gmp.py for 1 pubkey search. New Version is faster. Thanks to AlbertoBSD for a lot of discussion and help :) 

Older version is bsgs_algo_modified.py.
Use bsgs_algo_modified_multi.py for many pubkey search from a text file.

[Tips : bc1q39meky2mn5qjq704zz0nnkl0v7kj4uz6r529at ]

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
PVK not found. 500.00000 Billion scanned in 0.22 sec. New range [+] k1: 0xedbcef742b5352fbf62db07cb906b3
PVK not found. 500.00000 Billion scanned in 0.22 sec. New range [+] k1: 0xc7281c3ef86a5c66f0c01123f44718
PVK not found. 500.00000 Billion scanned in 0.21 sec. New range [+] k1: 0xd31c7496d76e14a47551350b06426a
PVK not found. 500.00000 Billion scanned in 0.22 sec. New range [+] k1: 0xcb0cd1053fd524d211d00bb80479e6
PVK not found. 500.00000 Billion scanned in 0.22 sec. New range [+] k1: 0xcdf5883c269b83a670f898d21f8ba5
PVK not found. 500.00000 Billion scanned in 0.22 sec. New range [+] k1: 0xe217393d344ff0cbbde8a588e13bc1
PVK not found. 500.00000 Billion scanned in 0.22 sec. New range [+] k1: 0xc6af67f2596faecee9745ad5573924
PVK not found. 500.00000 Billion scanned in 0.20 sec. New range [+] k1: 0x9b53550c290a6558eefdc6a2c9816f
PVK not found. 500.00000 Billion scanned in 0.22 sec. New range [+] k1: 0xac43ca1fcc20530fffb931f8357fcf
PVK not found. 500.00000 Billion scanned in 0.21 sec. New range [+] k1: 0xcc731c81f662f6802cc96c3267a487
PVK not found. 500.00000 Billion scanned in 0.18 sec. New range [+] k1: 0xf18a4b5982a5261f6382776f981dd2
PVK not found. 500.00000 Billion scanned in 0.18 sec. New range [+] k1: 0xf1c99d852a2f853f5eb188de8c2b2f
```
