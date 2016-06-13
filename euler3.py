'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

factors = []
goal = 600851475143

def factor(target):
    # access global variable factors
    global factors
    
    logger.info('  Factoring %s' % target)
    # Find the lowest denominator
    for n in range(2, target + 1):
        # If n is a factor, append to list
        if target % n == 0:
            logger.info('  %s is a factor of %s' % (n, target))
            factors.append(n)
            break
    new_target = target // factors[-1]
    logger.debug('  new target is %s' % new_target)
    if new_target > 1:
        logger.debug('repeating the factoring')
        factor(new_target)
    return factors
  

logger.info('  The factors of %s are %s' % (goal, factors))

def largest_factor(target):
    all_factors = factor(target)
    result = 0
    for num in all_factors:
        if num > result:
            result = num
    return result

logger.info('  The largest factor of %s is %s' % (goal, largest_factor(goal)))
