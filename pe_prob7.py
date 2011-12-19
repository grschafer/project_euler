# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10,001st prime number?

# easier solution: http://www.wolframalpha.com/input/?i=10001st+prime

def nth_prime(n):
    # edge case so I can increment by 2 and
    # avoid checking primality of even numbers
    if n == 1:
        return 2
    
    
    i = 1
    candidate = 1
    # store primes in a list for dividing later prime candidates
    primes = [2]
    
    # while we're not at nth prime
    while i < n:
        candidate += 2
        b = 0
        
        # loop through list of primes to see if they're factors of candidate
        while b < len(primes) and candidate % primes[b] != 0:
            b += 1
        
        # if no factor was found, candidate is a prime number
        if b == len(primes):
            primes.append(candidate)
            i += 1
    
    return candidate

def main():
    print(nth_prime(10001))
        
if __name__=='__main__':
    main()