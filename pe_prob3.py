# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import math

num = 600851475143

i = 2

while i < num:
    if num%i == 0:
        num /= i
    else:
        i += 1

print num