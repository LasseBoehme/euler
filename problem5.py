"""
github test

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of
the numbers from 1 to 20?
"""

check_nums = [x for x in range(1, 21)]

for n in range(0, 1000000000, 2520):
    if all(n % c == 0 for c in check_nums):
        print(n)
