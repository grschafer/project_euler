# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


# return a list of the numbers factors (in ascending order)
def factor(num):
    i = 2
    factors = []

    while i <= num:
        if num%i == 0:
            num /= i
            factors.append(i)
        else:
            i += 1
    
    return factors    

# find least common multiple of any list of numbers
def find_lcm(number_list):
    myfactors = {}
    
    for i in number_list:
        ifactors = factor(i)
        print "factors of",i," ",ifactors
        for x in ifactors:
            if x not in myfactors:
                myfactors[x] = 1
            if ifactors.count(x) > myfactors[x]:
                myfactors[x] = ifactors.count(x)
    
    print myfactors
    
    product = 1;
    for x in myfactors.keys():
        product *= x**myfactors[x]
    print product
        

def main():
    a = [3,17,5,9,8,4]
    find_lcm(a)
        
if __name__=='__main__':
    main()