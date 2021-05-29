# v3_gmp_bloom
This was the Third Version of this program. Later on new version with faster speed have been included (bsgs_dll_gmp).

In this version, bsgs_v5_gmp.py script should bypass the RAM constraint by using bloom filter.
bPfile_2_bloom.py is used to convert the bPfile.bin created earlier into a bloomfilter file. this reduces the size.

Then bsgs_v5_gmp.py only uses this bloomfilter file to search for 1 pubkey. 
For ex. 400 million elements in the table only need 2GB bloomfilter file and therefore need only 2GB RAM.
You can prepare bigger table and hence bigger bloomfilter if the PC has more memory. It will be faster.

Another script "bsgs_hybrid_gmp.py" has been include to search multiple publickeys all Together (not 1 by 1). Here the script can search millions of pubkey at once but the speed reduces quickly. Although it is still faster than searching the address or HASH160.

```
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
```
