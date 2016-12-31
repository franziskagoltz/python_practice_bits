"""Return count number of prime numbers, starting at 2.

For example::

    >>> primes(0)
    []

    >>> primes(1)
    [2]

    >>> primes(5)
    [2, 3, 5, 7, 11]

"""

import math


def primes(count):
    """Return count number of prime numbers, starting at 2."""

    pass


def is_prime(num):
    """Checks if a number is prime or not"""

    if num < 2:
        return False

    if num == 2:
        return True

    for x in range(2, int(math.sqrt(num))+1):
        if num % x == 0:
            return False

    return True


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT WORK!\n"
