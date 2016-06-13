'''
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 x 99

Find the largest palindrome made from the product of two 3-digit numbers.
'''

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def prepare_number(number):
    '''
    prepares a number by turning it into a string, retuns the string
    '''
    n = str(number)
    logger.debug('  target number has a length of %s' % len(n))
    return n


def is_palindrome(number):
    '''
    checks to see if a number is a palindrome
    '''
    # Convert number to a string
    num = prepare_number(number)
    logger.debug('checking %s' % num)
    
    # TODO: Set up even/odd, for now test with odd numbers of digits
    num_length = len(num)
    # only need to go hafway, since we're working from the back too
    if num_length % 2 == 1:
        for i in range((num_length // 2) + 1):
            a = num[i]
            b = num[-(i + 1)]
            logger.debug('a: %s, b: %s' % (a, b))
            if a == b:
                pass
            else:
                return False
        return True
    else:
        for i in range(num_length // 2):
            a = num[i]
            b = num[-(i + 1)]
            logger.debug('a: %s, b: %s' % (a, b))
            if a == b:
                pass
            else:
                return False
        return True

result = 111
for a in range(100, 1000):
    for b in range(a, 1000):
        target = a * b
        logger.debug('a: %s, b: %s, product: %s' % (a, b, target))
        if is_palindrome(target) and target > result:
            logger.info(('a: %s, b: %s, target: %s' % (a, b, target)))
            result = target

print(result)
