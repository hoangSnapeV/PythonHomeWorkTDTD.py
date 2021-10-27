import math
#1a
def squaredRoot2_1a( x ):
    a = math.sqrt( x ) 
    return a

print("result =", squaredRoot2_1a(9))
print("result =", squaredRoot2_1a(16))

#1b 
def cau1_b( x ):
    a = x ** (1/3)
    return a
print("result1 = ", cau1_b(8))

#1c
def cau1_c( x ):
    a = x ** (2/3)
    return a
print("result2 = ", cau1_c(27)) 

#1d
def cau1_d( x ):
    a = (x ** 3) / 3 - (x ** 2) / 2 - 2 * x + 1/3
    return a
print("result4 = ", cau1_d(2)) 

#1e
def cau1_e( x ):
    a = (2 * (x ** 2) - 3) / (7 * x + 4)
    return a
print("result5 = ", cau1_e(2)) 

#1f
def cau1_f( x ):
    a = (5 * (x ** 2) + 8 * x - 3) / (3 * (x ** 2) + 2)
    return a
print("result6 = ", cau1_f(2)) 

#1g

def cau1_g( x ):
    a = math.sin(x)
    return a
print("result7 = ", cau1_g(math.pi / 2)) 

#1h

def cau1_h( x ):
    a = math.cos(x)
    return a
print("result8 = ", cau1_h(math.pi / 3)) 

#1i

def cau1_i( x ):
    a = math.pow(3, x)
    return a
print("result9 = ", cau1_i(2))

#1j

def cau1_j( x ):
    a = math.pow(10, - x)
    return a
print("result10 = ", cau1_j(1))

#1k

def cau1_k( x ):
    a = math.exp(x)
    return a
print("result11 = ", cau1_k(1))

#1l

def cau1_l( x ):
    a = math.log(x , 2)
    return a
print("result12 = ", cau1_l(1))

#1m
def cau1_m( x ):
    a = math.log(x , 10)
    return a
print("result13 = ", cau1_m(10))

#1n
def cau1_n( x ):
    e = math.exp(1)
    a = math.log(x, e)
    return a
print("result14 = ", cau1_n(3))







