"""
For fixed integers a, b, c, define the crazy function F(n) as follows:
F(n) = n - c for all n > b
F(n) = F(a + F(a + F(a + F(a + n)))) for all n <= b

Also, define S(a, b, c) = sum{n=0}^b F(n)

For example, if a = 50, b = 2000 and c = 40, then F(0) = 3240 and F(2000) = 2040.
Also, S(50, 2000, 40) = 5204240.

Find the last 9 digits of S(21**7, 7**21, 12**7).
"""

import matplotlib.pyplot as plt

A = 250
B = 5000
C = 10

#A = 21**7
#B = 7**21
#C = 12**7

def F(n : int) -> int:
    if n > B:
        return n - C
    else:
        return F(A + F(A + F(A + F(A + n))))


def S() -> int:
    sum = 0

    for n in range(0, B+1):
        sum += F(n)

    return sum

x_vals = range(0, 5000)
y_vals = []

for i in x_vals:
    y_vals.append(F(i))

plt.plot(x_vals, y_vals)
plt.show()

#print(F(0))
#print(F(1))
#print(": " + str(F(2000)))
#print(S())
