import math

def is_prime(x):
    #check for anything less than 2, including negative numbers
    if x < 2:
        return False
    # 2 is prime but is to small for our for loop
    elif x == 2:
        return True
    else:
        # loop from 2 to the square root of x plus 1 (so we don't work too hard :P)
        for n in range(2, int(math.sqrt(x)) + 1):
            print n
            if x % n == 0:
                return False
        #if the for loop ends without perfect division the number must be prime
        return True

print is_prime(7)