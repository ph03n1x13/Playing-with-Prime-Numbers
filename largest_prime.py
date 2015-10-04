"""
                 ----------------------------------------------------------------
                |code for finding out the largest prime factor of a given number.|
                 ---------------------------------------------------------------
We need a sieve to filter the prime factors upto the given number's square root.
Then we'll determine the largest prime by repeatedly dividing the given number
the primes upto its square root and checking if the divisors are largest prime number.
------------------------------------------------------------------------------------------
 0 1 2 3 4 5 6 7 8 9 10
|-|-|-|-|-|-|-|-|-|-|-|

length of array is (10+1 = 11)
largest prime = square_root_of(len(array)-1)
 => (square_root_of(11-1))
 =>(square_root_of(10))
 and moreover  that 10 is on the len(array-1) = (11-1) = 10th index
 ------------------------------------------------------------------------------------------
 Cordial thanks to : Md Imrul Hassan Bhai for giving his valuable time. <3
"""
import math


def sieve_of_eratosthenes(sieve_len):
    sieve = [True] * sieve_len   # assume all the indexes (0 to sqrt(given_num)) contain prime numbers
    sieve[0] = sieve[1] = False
    largest_prime = int(math.sqrt(sieve_len-1))
    for prime in xrange(2, largest_prime+1):  # prime <= largest_prime
        if sieve[prime]:
            for not_primes in xrange(prime+prime, sieve_len, prime):
                sieve[not_primes] = False
    return sieve  # return the filtered or sieved array


def check_largest_prime_factor(filtered_array, given_number):
    prime_factors = []
    for prime in xrange(len(filtered_array)):
        while filtered_array[prime] and given_number % prime == 0: # notice we used the index number
            given_number /= prime  # that is given_number = given_number / prime
            prime_factors.append(prime)
    if given_number > 1:
        prime_factors.append(given_number)
    return prime_factors
test_number = int(raw_input("give number: "))
sqr_tstnum = int(math.sqrt(test_number))
filtered = sieve_of_eratosthenes(sqr_tstnum+1)  # we need 1 more index to cover the root
output = check_largest_prime_factor(filtered, test_number)
print output









