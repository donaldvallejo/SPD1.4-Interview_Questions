# Given a 32-bit signed integer, reverse digits of an integer.

# assume we stay at a 32 bit range
# assume that the function returns 0 

# check if value is greater than 10
# if it is less than the power of 31 return 

def reverse(self, x):     
    if abs(x) < 10: return x
    r = int(str(abs(x))[::-1])
    if r >= pow(2, 31): return 0
    return r if x > 0 else -r