import math
import sympy as sp

def even_function(f, x):
    if f(-x) == f(x):
        return True
    else:
        return False
def odd_function(f, x):
    if f(-x) == - f(x):
        return True
    else:
        return False

x = sp.symbols('x')
f = lambda x : 2 * x + 1

print(f(2))
print("Day là ham chan: ", even_function(f, x))
print("Day là ham le: ",odd_function(f, x))


