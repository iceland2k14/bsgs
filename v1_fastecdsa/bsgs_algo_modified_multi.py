# -*- coding: utf-8 -*-
"""

@author: iceland
"""
import bit
import time
import random
import math
import os
from fastecdsa import curve
from fastecdsa.point import Point

bs_file = 'baby_steps_table.txt'
f1 = 'test_pubkeys.txt'

publist = [line.split()[0] for line in open(f1,'r')]
total_pubkeys = len(publist)
print('Read {0} pubkeys from Target file'.format(total_pubkeys))


def Pub2Point(public_key):
    x = int(public_key[2:66],16)
    if len(public_key) < 70:
        y = bit.format.x_to_y(x, int(public_key[:2],16)%2)
    else:
        y = int(public_key[66:],16)

    return Point(x, y, curve=curve.secp256k1)

###############################################################################
# 10K btc 1KVyYVs7qbzuZt4s6M1hKRwtQZm2QQZLiA
# public_key = '0436b2b125c8feea47f32ca037faf154df3409c1cbf636584fcdef091e70fd7f3bf3400f3d8abf45916790a5f2618adfa87c6f8e050c19ea61248f15a4f1918cc3'
Qlist = [Pub2Point(public_key) for public_key in publist]
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


# start time
st = time.time()
###############################################################################

def lookup_in_baby_steps(S_list, k1, step, total_found_keys):
    Sx_dict = {line.x:k for k, line in enumerate(S_list)}
    intersection = Sx_dict.keys() & baby_steps.keys()
    if intersection != set():
        for line in intersection:
            b = baby_steps.get(line)
#            print('line', hex(line))
#            print('step', step)
#            print('b', b)
#            print('k1', k1)
            print("BSGS FOUND PrivateKey  : {0}".format(hex(k1 + step + b + 1)))
            total_found_keys += 1
            del S_list[Sx_dict.get(line)]
            del Sx_dict[line]
            
    return S_list, total_found_keys

def lookup_in_infinity(S_list, k1, step, total_found_keys):
    for line in S_list:
        if line == Point.IDENTITY_ELEMENT:
            print("BSGS FOUND PrivateKey  : {0}".format(hex(k1)))
            total_found_keys += 1
    return total_found_keys

          
def findkeys(PointList, k1, k2, k1G, mG, total_found_keys):
    step = 0
    S = [pp - k1G for pp in PointList]
    nb_keys = lookup_in_infinity(S, k1, step, total_found_keys)         # Point at Infinity
    total_found_keys = nb_keys
    
    while total_found_keys <  total_pubkeys and step<(1+k2-k1):
        S, nb_keys = lookup_in_baby_steps(S, k1, step, total_found_keys)
        total_found_keys = nb_keys
        S = [pp - mG for pp in S]   # Giant step
        step = step + m
            
    return PointList, total_found_keys
###############################################################################
total_found_keys = 0


while total_found_keys < total_pubkeys: 
    # We have to solve P = k.G, we know that k lies in the range ]k1,k2]
#    k1 = random.randint(1, curve.secp256k1.q//2)        # if you want to start from a random key
    k1 = 1                                              # if you want to start from 1 
    k2 = k1 + m*m
    print('Checking {0} keys from {1}'.format(m*m, hex(k1)))
    # m = math.floor(math.sqrt(k2-k1))
    
    k1G = k1 * G
    mG = m * G
    
    Qlist, total_found_keys = findkeys(Qlist, k1, k2, k1G, mG, total_found_keys)
    time_taken = time.time()-st
    print("Time Spent : {0:.2f} seconds. Speed {1:.2f} Keys/s".format(time_taken, (k2-k1)/time_taken))
    st = time.time()

print('All PrivateKeys Found. Finished Searching')

