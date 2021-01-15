# bsgs
Find PrivateKey of corresponding Pubkey(s) using BSGS algo.
Python3 implementation Using 1 thread. 

First time the program will create a table file in the same folder with name "baby_steps_table.txt" and will take some time.
Next time onwards this file will be directly used.

Use bsgs_algo_modified.py for 1 pubkey search.
Use bsgs_algo_modified_multi.py for many pubkey search from a text file.

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
BSGS FOUND PrivateKey  : 0x1312b2f
BSGS FOUND PrivateKey  : 0x17e2551e
All PrivateKeys Found. Finished Searching
Time Spent : 15.90 seconds
```
