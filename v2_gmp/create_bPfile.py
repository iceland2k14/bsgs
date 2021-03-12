# -*- coding: utf-8 -*-
"""

@author: iceland
"""
import sys
import gmp_ec as ec
import os
import math

G = ec.G

def create_table(start_value, end_value):
    # create a table:  f(x) => G * x
    P = ec.Scalar_Multiplication(start_value, G)
    baby_steps = []
    for x in range(start_value, end_value):
        baby_steps.append(P.x)
        P = ec.Point_Addition(P, G)
    baby_steps.append(P.x)              # last element
    return baby_steps


if len(sys.argv) > 3 or len(sys.argv) < 3:
    print('[+] Program Usage.... ')
    print('{} <bP items> <output filename>\n'.format(sys.argv[0]))
    print('Example to create a File with 20 million items:\n{} 20000000 bPfile.bin'.format(sys.argv[0]))
    sys.exit()


total = int(sys.argv[1])
bs_file = sys.argv[2]
out = open(bs_file, 'wb')
chunk = 1000000
print('\n[+] Program Running please wait...')

# =============================================================================
seq = range(1, total+1)
parts_list = [seq[i * chunk:(i * chunk) + chunk] for i in range(math.ceil(len(seq) / chunk))]

print('[+] Created {} Chunks ...'.format(len(parts_list)))
k = 1
for piece in parts_list:
    print('[+] Working on Chunk {} ...'.format(k), end='\r')
    start_value = min(piece)
    end_value = max(piece)
    baby_steps = create_table(start_value, end_value)
    for line in baby_steps:
        out.write(bytes.fromhex(hex(line)[2:].zfill(64)))
    out.flush()
    os.fsync(out.fileno())
    k += 1

out.close()
print('[+] File created successfully\n')