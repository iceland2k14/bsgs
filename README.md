# bsgs
Find PrivateKey of corresponding Pubkey(s) using BSGS algo.
Python3 implementation Using 1 thread. 

First time the program will create a table file in the same folder with name "baby_steps_table.txt" and will take some time.
Next time onwards this file will be directly used.

Use bsgs_v4_gmp.py for 1 pubkey search. Older version is bsgs_algo_modified.py.
Use bsgs_algo_modified_multi.py for many pubkey search from a text file.

Tips: bc1q39meky2mn5qjq704zz0nnkl0v7kj4uz6r529at

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

(base) C:\anaconda3>python bsgs_v4_gmp.py
[+] Starting Program : BSGS mode
[+] Reading Baby table from file complete in : 1.48287 sec
[+] seq value: 8000000000000    m value : 40000000
[+] k1: 0xc4940ff125dfd697b688394fcfa042
PVK not found. 8.00000 Trillion scanned in 1.16 sec. New range [+] k1:0xf321fcacfd15b0a80c158261a299bd
PVK not found. 8.00000 Trillion scanned in 1.22 sec. New range [+] k1:0x972da340730e643e6e876aa9ec5a7f
PVK not found. 8.00000 Trillion scanned in 1.17 sec. New range [+] k1:0x80a2c0b81727fa42febf9508f72246
PVK not found. 8.00000 Trillion scanned in 1.12 sec. New range [+] k1:0xfe9632542537987113dd294ef9018a
PVK not found. 8.00000 Trillion scanned in 1.12 sec. New range [+] k1:0xcfd9fa14f15ed649882dacc600ae33
PVK not found. 8.00000 Trillion scanned in 1.16 sec. New range [+] k1:0x87b2bfb79fa82f2ce7df71e979f7d7
PVK not found. 8.00000 Trillion scanned in 1.13 sec. New range [+] k1:0xf2a20260088a5a6ddb2bbfacd42f21
PVK not found. 8.00000 Trillion scanned in 1.11 sec. New range [+] k1:0xdd3eceba55412cca6592ebcfaa2a33
PVK not found. 8.00000 Trillion scanned in 1.16 sec. New range [+] k1:0xfa23c3aea823f49fb37d4f0c598e8f
PVK not found. 8.00000 Trillion scanned in 1.13 sec. New range [+] k1:0xef14cef41502bd4a0257d73d670b34
PVK not found. 8.00000 Trillion scanned in 1.20 sec. New range [+] k1:0xc47b9d5c79b572499c56ed736dfe70
PVK not found. 8.00000 Trillion scanned in 1.11 sec. New range [+] k1:0xb1ea592b2f29153d97048732924849
PVK not found. 8.00000 Trillion scanned in 1.12 sec. New range [+] k1:0xf8fa2c94985aa35d48967c4de3346c
PVK not found. 8.00000 Trillion scanned in 1.13 sec. New range [+] k1:0xac36194822c827350e18eb5a88dc0c
PVK not found. 8.00000 Trillion scanned in 1.16 sec. New range [+] k1:0xb9dc6d73148bc52a451e27d49e9f77
PVK not found. 8.00000 Trillion scanned in 1.12 sec. New range [+] k1:0xf8e093ff45c7fdc57901618a36dbdf
PVK not found. 8.00000 Trillion scanned in 1.18 sec. New range [+] k1:0xae9e409b599063b98fb029599987fc
PVK not found. 8.00000 Trillion scanned in 1.21 sec. New range [+] k1:0x9b9439ece24a4fe1cd35de727391be
PVK not found. 8.00000 Trillion scanned in 1.36 sec. New range [+] k1:0x8ee59bea8aad44ffe8e745ddf0f4a3
PVK not found. 8.00000 Trillion scanned in 1.10 sec. New range [+] k1:0xba50d1490dd79d1d30807ae5a1309b
PVK not found. 8.00000 Trillion scanned in 1.24 sec. New range [+] k1:0xea0f892afe782702ccb672570cc31f
```
