import math

def factorial(a):
    result = a
    for i in range(a-1, 0, -1):
        result *= i
    return result


def log(a):
    return math.log(a)        

