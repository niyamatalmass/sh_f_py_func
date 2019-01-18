'''
Prime factors means in Bangali is "মৌলিক উত্পাদক"
The prime factors of 6 is 3*2 where 3 and 2 are prime numbers.
We have to find those two prime numbers( prime numbers means can't factorize into samller number ) that's multiply produces the n
'''




def prime_factors(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    d = 2 
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1: factors.append(n)
            break
    return factors