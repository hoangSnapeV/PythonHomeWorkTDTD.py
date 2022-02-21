import math
import sympy as sp

def cau_a(f, x):
    if f(-x) == f(x):
        print("Ham so chan")
    else:
        print("Ham so le")

x = sp.symbols('x')
f = lambda x : x ** (-5)

print(f(2))
print(cau_a(f, x))




