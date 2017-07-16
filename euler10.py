"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
# Use sieve of eratastothenes?
max_number = 2000000

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

status_list = [True for x in range(2, max_number + 1)]
logging.debug(status_list)

for test_number in range(2, max_number + 1):
    for flipper in range(test_number * 2, max_number + 1, test_number):
        status_list[flipper-2] = False

logging.debug(status_list)

primes = [x for x in range(2, max_number + 1) if status_list[x-2] == True]

logging.info(primes)

total = 0

for n in primes:
    total += n

logging.info("answer is {}".format(total))