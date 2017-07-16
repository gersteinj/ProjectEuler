"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from math import sqrt

target = 1000

for a in range(1, 500):
    for b in range(a, 500):
        c = 1000 - a - b
        logging.debug("{} {} {}".format(a, b, c))
        if c == sqrt(a ** 2 + b ** 2):
            logging.info("Solution found! a: {}, b: {}, c: {}".format(a, b, c))
            logging.info("product: {}".format(a*b*c))