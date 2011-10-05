# The sum of the squares of the first ten natural numbers is,
#       1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
#       (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


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