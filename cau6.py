
import numpy as np

x = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

#cau6a
x_6first = x[0:6]
print(x_6first)

#cau6b
x_5Last = x[len(x) - 5:len(x)]
# x_5Last = [-5,len(x)]
print(x_5Last)

#cau6c
x_1_4_last = x[ [0, 3, len(x) - 1]]

print(x_1_4_last)

#cau6d
x_1_3_5_7 = x[ [0, 2, 4, 6]]

print(x_1_3_5_7)

#cau6e
x_odds = x[0: len(x): 2]
print(x_odds)


