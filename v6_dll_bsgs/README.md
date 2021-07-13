## Usage
```python bsgs_create_bpfile_bloomfile.py 400000000 bpfile.bin bloomfile.bin 4```  
_This uses 4 cpu to make bPfile and bloomfile with 400 million items._  

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

```
