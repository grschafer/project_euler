# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?


# DO NAIVE/BRUTE FORCE OR PICK A WIKIPEDIA ALG TO IMPLEMENT?

# sum is (n * (n + 1) / 2), then square it
def sq_of_sum(n):
    return (n * (n + 1) / 2)**2

def sum_of_sq(n):
    sum = 0
    for i in range(n + 1):
        sum += i*i
    return sum

def main():
    print sq_of_sum(100) - sum_of_sq(100)
        
if __name__=='__main__':
    main()