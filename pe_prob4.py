# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# based on using time.clock():
#   brute_force_multiplication method takes ~0.40 seconds
#   divide_given_palindrome method takes ~0.010 seconds
#   divide_given_palindrome method takes ~0.096 seconds if it runs through all of the given palindromes

import time

# generates palindromes in descending order
def get_next_palindrome():
    next_pal = str(get_next_palindrome.count) + str(get_next_palindrome.count)[::-1]
    get_next_palindrome.count -= 1
    return int(next_pal)
get_next_palindrome.count = 999


def divide_given_palindrome(pal):
    for i in range(100,1000):
        if pal%i == 0:
            num = pal/i
            if num > 99 and num < 1000:
                return pal
    return False


def is_palindrome(num):
    num = str(num)
    return num[0] == num[-1] and num[1] == num[-2] and num[2] == num[-3]

def brute_force_multiplication():
    best = "-1"
    for i in range(100, 1000):
        for j in range(100, 1000):
            prod = str(i*j)
            if (is_palindrome(prod) and int(prod) > int(best)):
                best = prod
    return best
        
def main():
    result = divide_given_palindrome(get_next_palindrome())
    while result is False:
        result = divide_given_palindrome(get_next_palindrome())
    print result
    # print(brute_force_multiplication())

if __name__=='__main__':
    # start = time.clock()
    main()
    # end = time.clock()
    # print(end - start)