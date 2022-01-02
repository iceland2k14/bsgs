## Usage
```python bsgs_create_bpfile_bloomfile.py 400000000 bpfile.bin bloomfile.bin 4```  
_This uses 4 cpu to make bPfile and bloomfile with 400 million items._  

```python bsgs_dll_search.py -pfile PubKeys.txt -b bpfile.bin -bl bloomfile.bin -rand1```  
_This is the main script to search all pubkeys together using 1 cpu_

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



(base) C:\anaconda3>python bsgs_dll_search.py -b bp00.bin -bl bl00.bin -p 04CB2DA061F7C5A8178651A0BBA315B7AF83CBA3EB4EC7553F81A1F4C58C7BB3613C6758765787DC03C7D079169A780A9421C902DB098B1EE7BB527954BC50C318 -keyspace F0001000000000001:F0001000500000001

[+] Starting Program : BSGS mode     Version [ 02012022 ]
[+] Search Started for the Public key:  04cb2da061f7c5a8178651a0bba315b7af83cba3eb4ec7553f81a1f4c58c7bb3613c6758765787dc03c7d079169a780a9421c902db098b1ee7bb527954bc50c318
[+] Search Mode: Sequential search in the given range
[+] Reading bloom filter from file complete in : 0.03099 sec
[+] Reading Baby table from file complete in : 0.00100 sec
[+] seq value: 50000000000000    m value : 10000000
[+] Search Range: 0xf0001000000000001  to  0xf0001000500000001
                                                                [+] k1: 0xf0001000000000001
============== KEYFOUND ==============
BSGS FOUND PrivateKey  0xf0001000000000002
======================================
Search Finished. All pubkeys Found !
```
