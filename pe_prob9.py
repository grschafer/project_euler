# A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
#       a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

from bisect import bisect_left

def gen_n_powers(n):
    powers = [0 for i in range(n)]
    for i in range(n):
        powers[i] = i**2;
    return powers

def find_pythagorean_triplet_eq_n(n, powers):
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            c2 = powers[i] + powers[j]
            idx = bisect_left(powers, c2, lo=j)
            if idx < n and powers[idx] == c2:
                if sum((i,j,idx)) == n:
                    return (i,j,idx)
    return 0
    
def main():
    n = 1000000
    powers = gen_n_powers(n)
    triplet = find_pythagorean_triplet_eq_n(n, powers)
    print triplet
    print reduce(lambda x,y: x*y, triplet)
        
if __name__=='__main__':
    main()

