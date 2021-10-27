import math
import numpy as np

def cau2_a( x ):
    a = 2 + (x ** 2) / (x ** 2 + 4)
    return a

fmin = math.inf
fmax = - math.inf

for x in np.arange( -2, 2.1, 0.1 ):
    b = cau2_a( x )
    if b < fmin:
        fmin = b
    if b > fmax:
        fmax = b
    print(cau2_a( x ))

print("max = ", fmax)
print("min = ", fmin)
print("-----------------------------------aaaa")

#2b
def cau2_b( x ):
    a = math.sqrt(5 * x + 10)
    return a

fmin_b = math.inf
fmax_b = - math.inf

for x in np.arange( 0, 5, 0.1 ):
    b = cau2_b( x )
    if b < fmin_b:
        fmin_b = b
    if b > fmax_b:
        fmax_b = b
    print(cau2_b( x ))

print("max = ", fmax_b)
print("min = ", fmin_b)

print("-----------------------------------bbb")
#2c
def cau2_c( x ):
    a = 2 / (x ** 2 - 16)
    return a

fmin_c = math.inf
fmax_c = - math.inf

for x in np.arange( 5, 10, 0.1 ):
    b = cau2_c( x )
    if b < fmin_c:
        fmin_c = b
    if b > fmax_c:
        fmax_c = b
    print(cau2_c( x ))
print("max_c = ", fmax_c)
print("min_c = ", fmin_c)

print("---------------=-------------ccc")


#2d
def cau2_d( x ):
    a = x ** 4 + 3 * (x ** 2) - 1
    return a

fmin_d = math.inf
fmax_d = - math.inf

for x in np.arange( -3, 3.1, .1 ):
    b = cau2_d( x )
    if b < fmin_d:
        fmin_d = b
    if b > fmax_d:
        fmax_d = b
    print(cau2_d( x ))
print("max_d = ", fmax_d)
print("min_d = ", fmin_d)

print("---------------=-------------ddd")

#2e
def cau2_e( x ):
    if x >= 0:
        return x
    else:
        return -x

fmin_e = math.inf
fmax_e = - math.inf

for x in np.arange( -3, 3.1, .1 ):
    b = cau2_e( x )
    if b < fmin_e:
        fmin_e = b
    if b > fmax_e:
        fmax_e = b
    print(cau2_e( x ))
print("max_e = ", fmax_e)
print("min_e = ", fmin_e)

print("---------------=-------------eee")


#2f
def cau2_f( x ):
    if x > 1:
        return 1
    elif x >= 0:
        return x ** 2
    else:
        return -x

fmin_f = math.inf
fmax_f = - math.inf

for x in np.arange( -3, 3.1, .1 ):
    b = cau2_f( x )
    if b < fmin_f:
        fmin_f = b
    if b > fmax_f:
        fmax_f = b
    print(cau2_f( x ))
print("max_f = ", fmax_f)
print("min_f = ", fmin_f)

print("---------------=-------------fff")







