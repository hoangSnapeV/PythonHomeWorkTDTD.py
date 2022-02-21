#cau2a 
import numpy as np
n = 5

b = [12 + i * 2 for i in np.arange(0, n)]
print('b = ', b)

#cau2b

c = [31 + i * 2 for i in range(n)]
print('c = ', c)

#cau2c

x = [i for i in np.arange(-n, n + 1)]
print('x = ', x)

#cau2d

y = [-i for i in np.arange(-n, n + 1)]
print('y = ', y)

#cau2e

z = [10 - i * 2 for i in np.arange(0, 8)]
print('z = ', z)

#cau2f
w = [1]
for i in range(2, 14, 2):
    w.append(1.0 / i)
print('w = ', w)


#cau2g
d = [1, 1]
for i in range(2, n):
    d.append(d[i - 1] + d[i - 2])

d_final = [1.0 / d[i] for i in range(len(d))]

print('d = ',d_final)

#cauh
#b1 tim so nguyen tố
n = 30
#print(int(3 / 2) + 1)
h = []
count = 0
for i in range(1, n):
    for k in range(1, int(n / 2) + 1):
        if(i % k == 0):
            count += 1
    if(count > 2):
        count = 0
    else:
        h.append(i)   
        count = 0




print('h = ', h)
