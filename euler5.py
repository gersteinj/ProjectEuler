"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# start by getting factors
# multiply prime factors (maximum number of times each factor occurs)

answer = 1

def get_prime_factors(num):
    orig = num
    factors = []
    for testing in range(2, orig + 1):
        while num % testing == 0:
            factors.append(testing)
            num /= testing
    logging.debug("{}: {}".format(orig, factors))
    return factors

list_max = 20

list_of_factors = [get_prime_factors(x) for x in range(11, list_max + 1)]
print(list_of_factors)

# list_of_factors is the prime factors of each relevant number I'm checking for on the LCM
# Now I need to figure out how many times to use each prime factor

all_primes = {}
for l in list_of_factors:
    for item in l:
        if item not in all_primes:
            all_primes[item] = 0

print(all_primes)

for key, value in all_primes.items():
    for l in list_of_factors:
        if l.count(key) > value:
            value = l.count(key)
    logging.debug("The largest number of occurences of {} is {}".format(key, value))
    answer *= (key ** value)

print(answer)


"""
# Works for small lists, but is too slow
test_list = [6, 7, 8, 9, 10]
list_max = test_list[-1]
current_num = list_max
# current_num = 2520

def check_list(list_to_check):
    global current_num
    for n in test_list:
        logging.debug("testing {} with {}: {}".format(current_num,n,current_num%n == 0))
        if current_num % n != 0:
            break
    else:
        logging.debug("made it to the end, the answer is {}".format(current_num))
        return True

while not check_list(test_list):
    current_num += list_max"""