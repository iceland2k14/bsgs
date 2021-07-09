# -*- coding: utf-8 -*-
"""
Create bpfile.bin using multi_cpu

Usage :
 > python create_bPfile_mcpu.py 20000000 mybPfile.bin 4

@author: iceland
"""
import sys
import gmp_ec as ec
import os
from itertools import islice 
import math
from multiprocessing import Pool

G = ec.G


def create_table(this_list):
    start_value, end_value, m = this_list
    print('[+] Working on Chunk {} ...'.format(m))
    # create a table:  f(x) => G * x
    P = ec.Scalar_Multiplication(start_value, G)
    baby_steps = []
    for x in range(start_value, end_value):
        baby_steps.append(P.x)
        P = ec.Point_Addition(P, G)
    baby_steps.append(P.x)              # last element
    return baby_steps

def table_wrapper(data):
    create_table(*data)     
# =============================================================================
if __name__ == '__main__':
    if len(sys.argv) > 4 or len(sys.argv) < 4:
        print('[+] Program Usage.... ')
        print('{} <bP items> <output filename> <Number of cpu>\n'.format(sys.argv[0]))
        print('Example to create a File with 20 million items using 4 cpu:\n{} 20000000 bPfile.bin 4'.format(sys.argv[0]))
        sys.exit()

    total = int(sys.argv[1])
    bs_file = sys.argv[2]
    num_cpu = int(sys.argv[3])
    out = open(bs_file, 'wb')
    chunk = 1000000
    print('\n[+] Program Running please wait...')
    
    
    seq = range(1, total+1)
    parts_list = [seq[i * chunk:(i * chunk) + chunk] for i in range(math.ceil(len(seq) / chunk))]
    print('[+] Created Total {} Chunks ...'.format(len(parts_list)))
    
    parts_list = [(min(line), max(line), k+1) for k, line in enumerate(parts_list)]
    nn = iter(parts_list)
    subdata = [list(islice(nn, num_cpu)) for m in range((len(parts_list)//num_cpu)+1)]
    
#    p_list = [ [1+i * chunk,(i * chunk) + chunk, i+1 ] for i in range((total//chunk)+1)]
    
    k = 1
    
    while k <= len(subdata):
        
        pool = Pool(processes=num_cpu)
        results = pool.map(create_table, subdata[k-1])
            
        for mm in range(len(results)):
            for line in results[mm]:
                out.write(bytes.fromhex(hex(line)[2:].zfill(64)))
            out.flush()
            os.fsync(out.fileno())
        pool.close()
        
        k += 1
        
        
    out.close()
    print('[+] File created successfully\n')