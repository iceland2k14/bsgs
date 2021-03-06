# -*- coding: utf-8 -*-
"""

@author: iceland
"""
import bit
import time
import random
import os
from fastecdsa import curve
from fastecdsa.point import Point

bs_file = 'baby_steps_table.txt'

def Pub2Point(public_key):
    x = int(public_key[2:66],16)
    if len(public_key) < 70:
        y = bit.format.x_to_y(x, int(public_key[:2],16)%2)
    else:
        y = int(public_key[66:],16)

    return Point(x, y, curve=curve.secp256k1)

###############################################################################
# Puzzle 46 : Privatekey Key 0x2ec18388d544
public_key = '04fd5487722d2576cb6d7081426b66a3e2986c1ce8358d479063fb5f2bb6dd5849a004626dffa0fb7b934118ea84bacc3b030332eee083010efa60025e4fde7297'
Q = Pub2Point(public_key)
G = curve.secp256k1.G

###############################################################################
def create_table(m):
    # create a table:  f(x) => G * x
    P = G
    baby_steps = []
    for x in range(m):
        baby_steps.append(P.x)
        P = P + G
    return baby_steps

###############################################################################

m = 10000000    # default value

valid = os.path.isfile(bs_file)
if valid == True:
    print('\nFound the Baby Steps Table file: '+bs_file+'. Will be used directly')
    baby_steps = {int(line.split()[0],10):k for k, line in enumerate(open(bs_file,'r'))}
    if m != len(baby_steps) and not len(baby_steps) == 0: 
        m = len(baby_steps)
        print('Taken from table. m is adjusted to = ', m)
    if len(baby_steps) == 0 :
        print('Size of the file was 0. It will be created and overwritten')
        valid = False
if valid == False:
    print('\nNot Found '+bs_file+'. Will Create This File Now. \
          \nIt will save to this file in the First Run. Next run will directly read from this file.')
    out = open(bs_file,'w')
    baby_steps = create_table(m)
    for line in baby_steps: out.write(str(line) + '\n')
    out.close()
    baby_steps = {line:k for k, line in enumerate(baby_steps)}

# We have to solve P = k.G, we know that k lies in the range ]k1,k2]
# k1 = random.randint(1, curve.secp256k1.q//2)    # if you want to start from a random key
k1 = 1                                          # if you want to start from 1 
k2 = k1 + m*m
print('Checking {0} keys from {1}'.format(m*m, hex(k1)))
# m = math.floor(math.sqrt(k2-k1))

# start time
st = time.time()
###############################################################################
k1G = k1 * G
mG = m * G
def findkey(onePoint):
    S = onePoint - k1G
    if S == Point.IDENTITY_ELEMENT: return k1    # Point at Infinity
    found = False
    step = 0
    while found is False and step<(1+k2-k1):
        if S.x in baby_steps:
#            b = baby_steps.index(S.x)  # if using list
            b = baby_steps.get(S.x)
            found = True
            break
        else:
            # Giant step
            S = S - mG
            step = step + m
    if found == True:
        final_key = k1 + step + b + 1
    else:
        final_key = -1
    return final_key
###############################################################################

final_key = findkey(Q)
if final_key >0: 
    print("BSGS FOUND PrivateKey  : {0}".format(hex(final_key)))
else:
    print('PrivateKey Not Found')


print("Time Spent : {0:.2f} seconds".format(time.time()-st))
