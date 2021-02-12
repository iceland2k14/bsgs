# -*- coding: utf-8 -*-
"""

@author: iceland
"""

import gmpy2


modulo	= 115792089237316195423570985008687907853269984665640564039457584007908834671663
order	= 115792089237316195423570985008687907852837564279074904382605163141518161494337
#modulo	= 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
#order	= 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
Gx	= 55066263022277343669578718895168534326250603453777594175500187360389116729240
Gy	= 32670510020758816978083085130507043184471273380659243275938904335757337482424


modulo	= gmpy2.mpz(modulo)
order	= gmpy2.mpz(order)
Gx	= gmpy2.mpz(Gx)
Gy	= gmpy2.mpz(Gy)

# =============================================================================
class Point:
	def __init__(self, x=0, y=0):		# Affine
		self.x = x
		self.y = y
# =============================================================================    
	def __str__(self):
		if self == self.IDENTITY_ELEMENT:
			return '<POINT AT INFINITY>'
		else:
			return 'X: 0x{:x}\nY: 0x{:x}'.format(self.x, self.y)
# =============================================================================        
	def __unicode__(self) -> str:
		return self.__str__()
# =============================================================================     
	def __repr__(self) -> str:
		return self.__str__()
# =============================================================================
	def __eq__(self, other) -> bool:
		return self.x == other.x and self.y == other.y
# =============================================================================        
	def __add__(self, other):
		if self == self.IDENTITY_ELEMENT:
			return other
		elif other == self.IDENTITY_ELEMENT:
			return self
		elif self == -other:
			return self.IDENTITY_ELEMENT
		else:
			return Point_Addition(Point(self.x,self.y), Point(other.x,other.y))
# =============================================================================    
	def __radd__(self, other):
		return self.__add__(other)
# =============================================================================    
	def __sub__(self, other):
		if self == other:
			return self.IDENTITY_ELEMENT
		elif other == self.IDENTITY_ELEMENT:
			return self

		negative = Point(other.x, -other.y % modulo)
		return self.__add__(negative)
# =============================================================================    
	def __mul__(self, scalar: int):
		if scalar == 0:
			return self.IDENTITY_ELEMENT

		mp = Scalar_Multiplication(scalar)

		if mp.x == 0 and mp.y == 0:
			return self.IDENTITY_ELEMENT
		return mp
# =============================================================================    
	def __rmul__(self, scalar: int):
		return self.__mul__(scalar)
# =============================================================================    
	def __neg__(self):
		if self == self.IDENTITY_ELEMENT:
			return self

		return Point(self.x, -self.y % modulo)
# =============================================================================

G = Point(Gx,Gy) 
Point.IDENTITY_ELEMENT = Point(0, 0)  # also known as the point at infinity
# =============================================================================

def Point_Addition(A, B, p=modulo):
	if A == Point.IDENTITY_ELEMENT: return B
	if B == Point.IDENTITY_ELEMENT: return A
	if A == -B: return Point.IDENTITY_ELEMENT
	if A.x == B.x and A.y == B.y: return Point_Doubling(A, p=modulo)
	R = Point()
	dx = B.x - A.x
	dy = B.y - A.y	
	c = dy * gmpy2.invert(dx, p) % p

	R.x = (c*c - A.x - B.x) % p
	R.y = (c*(A.x - R.x) - A.y) % p
	return R
# =============================================================================

def Point_Doubling(A, p=modulo):
	R = Point()
	c1 = A.x * A.x * gmpy2.invert(A.y+A.y, p)
	c = (c1 + c1 + c1) % p;

	R.x = (c*c - A.x - A.x) % p
	R.y = (c*(A.x - R.x) - A.y) % p
	return R
# =============================================================================

def Scalar_Multiplication(k, A=G, p=modulo):
	if k == 0: return Point.IDENTITY_ELEMENT
	elif k == 1: return A
	elif (k%2 == 0):
		return Scalar_Multiplication(k//2, Point_Doubling(A, p), p)
	else:
		return Point_Addition(A, Scalar_Multiplication( (k-1)//2, Point_Doubling(A, p), p), p)

# =============================================================================

# =============================================================================

def create_xpoint_table(start_value, end_value):
    # create a table:  f(x) => G * x
#    P = G * start_value                        # using operator overloading
    P = Scalar_Multiplication(start_value, G)
    baby_steps = []
    for x in range(start_value, end_value):
        baby_steps.append(int(P.x))
#        P = P + G                              # using operator overloading
        P = Point_Addition(P, G)
    return baby_steps
# =============================================================================

def Point_to_Pubkey(A, compressed=False):
    str_x = hex(A.x)[2:].zfill(64)
    if compressed == True:
        prefix = str(2 + int(A.y) % 2).zfill(2)
        suffix = ''
    else:
        prefix = '04'
        suffix = hex(A.y)[2:].zfill(64)
    return prefix + str_x + suffix
# =============================================================================

def bulkInversionModP(in_list):
    chain_list = []
    total = 1
    for i in range(len(in_list)):
        total = (total * in_list[i]) % modulo
        chain_list.append(total)

    inverse = gmpy2.invert(total, modulo)       # do single inversion

    for i in range(len(in_list)-1, -1, -1):     # Loop upto 0 with decrement
        if i > 0:
            newval = (chain_list[i-1] * inverse) % modulo
            inverse = (inverse * in_list[i]) % modulo
            in_list[i] = newval
        else:
            in_list[i] = inverse
    return in_list
# =============================================================================

def generateKeyPairsBulk(pvk_list):
    count = len(pvk_list)
    
    table = []            # generate a table of points G, 2G, 4G, 8G...(2^255)G
    table.append(G)
    for i in range(1, 256):
        table.append(Point_Doubling(table[i-1]))
    
    pub_list = [Point.IDENTITY_ELEMENT for i in range(count)]


    for i in range(256):
        runList = []
#        // calculate (Px - Qx)
        for j in range(count):
            k = pvk_list[j]
            if gmpy2.bit_test(k, i):
                if pub_list[j] == Point.IDENTITY_ELEMENT:
                    run = 2
                else:
                    run = (pub_list[j].x - table[i].x) % modulo
            else:
                run = 2
            
            runList.append(run)
        
#       // calculate 1/(Px - Qx)
        runList = bulkInversionModP(runList)
#       // complete the addition
        for j in range(count):
            k = pvk_list[j]
            if gmpy2.bit_test(k, i):
                if pub_list[j] == Point.IDENTITY_ELEMENT:
                    pub_list[j] = table[i]
                else:
                    rise = (pub_list[j].y - table[i].y) % modulo
#                   // s = (Py - Qy)/(Px - Qx)
                    s = rise * runList[j]
#                   //rx = (s*s - px - qx) % _p;
                    rx = ( s*s - pub_list[j].x - table[i].x ) % modulo
#                   //ry = (s * (px - rx) - py) % _p;
                    ry = ((s * (pub_list[j].x - rx)) % modulo - pub_list[j].y ) % modulo
                
                    pub_list[j] = Point(rx, ry)
    
    return pub_list
