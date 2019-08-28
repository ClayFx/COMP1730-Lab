## COMP1730/6730 S2 2019 - Homework 3
# Submission is due 11.55pm, Monday the 26th of August, 2019.

## YOUR ANU ID: u6234544
## YOUR NAME:   Xuan Feng

## You should implement the two functions `count_factors(n)` and
## `count_prime_factors(n)` below. The `pass` statement is only a
## placeholder which you should replace with your implementation.

def count_factors(n):
    """
    Then it checks whether the Integer i from [1 ... n] is a factor of n
    If n % i == 0, it means i is a factor of n.
    """
    # The function first checks whether the input is valid.
    if n <= 0:
        raise Exception("Inout Error")
    counter = 0
    for i in range(1, n+1):
        if n % i == 0:
            counter += 1
    return counter

def count_prime_factors(n):
    """The function first checks whether the input is valid.
       Then it checks whether the Integer i from [1 ... n] is a prime factor of n.
       A prime factor of n should be both a factor of n and a prime number"""
    if n <= 0:
        raise Exception("Inout Error")
    counter = 0
    for i in range(1, n+1):
        if n % i == 0 and is_prime(i):
            counter += 1
    return counter

def is_prime(n):
    '''
    Returns True if n is a prime number and False otherwise.
    n must be a positive integer.
    '''
    return count_factors(n) == 2

def test_count_factors():
    '''
    This function runs a number of tests of the count_factors function.
    If it works ok, you will just see the output ("all tests passed") at
    the end when you call this function; if some test fails, there will
    be an error message.
    '''
    assert count_factors(1) == 1
    assert type(count_factors(1)) == int
    assert count_factors(2) == 2
    assert type(count_factors(2)) == int
    assert count_factors(3) == 2
    assert type(count_factors(3)) == int
    assert count_factors(4) == 3
    assert type(count_factors(4)) == int
    assert count_factors(6) == 4
    assert type(count_factors(6)) == int
    assert count_factors(8) == 4
    assert type(count_factors(8)) == int
    assert count_factors(9) == 3
    assert type(count_factors(9)) == int
    assert count_factors(10) == 4
    assert type(count_factors(10)) == int
    assert count_factors(12) == 6
    assert type(count_factors(12)) == int
    print("all tests passed")

def test_is_prime():
    '''
    This function runs a number of tests of the is_prime function.
    If it works ok, you will just see the outp    counter = 0
    for i in range(1, n+1):
        if n % i == 0:
            counter += 1
    return counterut ("all tests passed") at
    the end when you call this function; if some test fails, there will
    be an error message.
    '''
    # test with known primes
    for n in (2,3,5,7,11,13,17,23):
        assert is_prime(n)
        assert type(is_prime(n)) == bool
    print("all tests passed")

def test_count_prime_factors():
    '''
    This function runs a number of tests of the count_prime_factors function.
    If it works ok, you will just see the output ("all tests passed") at
    the end when you call this function; if some test fails, there will
    be an error message.
    '''
    assert count_prime_factors(1) == 0
    assert type(count_prime_factors(1)) == int
    assert count_prime_factors(2) == 1
    assert type(count_prime_factors(2)) == int
    assert count_prime_factors(3) == 1
    assert type(count_prime_factors(3)) == int
    assert count_prime_factors(4) == 1
    assert type(count_prime_factors(4)) == int
    assert count_prime_factors(6) == 2
    assert type(count_prime_factors(6)) == int
    assert count_prime_factors(8) == 1
    assert type(count_prime_factors(8)) == int
    assert count_prime_factors(9) == 1
    assert type(count_prime_factors(9)) == int
    assert count_prime_factors(10) == 2
    assert type(count_prime_factors(10)) == int
    assert count_prime_factors(12) == 2
    assert type(count_prime_factors(12)) == int
    print("all tests passed")
