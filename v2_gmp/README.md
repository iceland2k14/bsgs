# v2_gmp
This was the Second Version of this program. Later on new version with faster speed have been included (v3_gmp_bloom and then bsgs_dll_gmp).

Use bsgs_v4_gmp.py for 1 pubkey search. Thanks to AlbertoBSD for a lot of discussion and help :) 

You need to first, create a baby table file (bPfile.bin) using the provided script "create_bPfile.py". Syntax is create_bPfile.py 20000000 bPfile.bin

Then use the script "bsgs_v4_gmp.py" for hunting the pubkey.
The constrained is RAM uasage here. It fills up very quickly with bigger bPfile for ex. 1 billion elements.

```
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
```
