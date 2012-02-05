# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.


def sieve(n):
    primes = set()
    for i in range(2, n):
        primes.add(i)
    for i in range(2, n):
        for j in range(i * 2, n, i):
            if j in primes:
                primes.remove(j)
    return primes
   
def main():
    n = 2000000
    primes = sieve(n)
    print(sum(primes))
        
if __name__=='__main__':
    main()

