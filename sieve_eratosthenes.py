"""
                     ---------------------------------------------------------------------------------
                     |A simple sieve of Eratosthenes simulated from a 100 index worksheet|
                     ----------------------------------------------------------------------------------
The snippet is not an ideal solution rather a visualisation of how a sieve works actually.
a nube's attempt albeit ;).   
"""


import math 
test_sieve = range(1000)
print len(test_sieve)

def sieve_of_eratosthenes(sieve):
    range_of_primes = int(math.sqrt(len(sieve)-1)) # we'll need the root of len(sv)-1 th index number
    sieve[0] = 'x'
    sieve[1] = 'x'
    for primes in xrange(2, range_of_primes+1, 1): # for(i =2; i<=range_of_primes; i++) {...}
        if sieve[primes] != 'x':
            not_prime_indexes = primes + primes
            while not_prime_indexes < len(sieve):
                sieve[not_prime_indexes] = 'x'
                not_prime_indexes += primes
    return sieve


def print_worksheet(array):  # for a stylish worksheet print out :P 
    layer1 = 0
    while layer1 < len(array):
        layer2 = 0
        while layer2 < 10 and layer1 < len(array):
            print array[layer1],
            layer1 += 1
            layer2 += 1
        print ""
a = sieve_of_eratosthenes(test_sieve)
print_worksheet(a)

