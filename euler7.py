"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
from math import sqrt

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

primes = [2]
how_many_primes = 10001

def check_primality(num):
    for x in range(2, int(sqrt(num)) + 1):
        if num % x == 0:
            return False
    return True

test_num = 3
while len(primes) < how_many_primes:
    if check_primality(test_num):
        primes.append(test_num)
    test_num += 2

print(primes)