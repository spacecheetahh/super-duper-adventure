import math

def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    else:
        for n in range(2, int(math.sqrt(x)) + 1):
            print n
            if x % n == 0:
                return False
        return True

print is_prime(7)