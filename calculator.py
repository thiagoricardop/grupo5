# Calculator - Group 5

import math

def factorial(a):
    result = a
    for i in range(a-1, 0, -1):
        result *= i
    return result


def log(a):
    return math.log(a)        

def power(base, exponent):
    return math.pow(base, exponent)

def division(numerator, denominator):
    if denominator == 0:
        raise ZeroDivisionError("Erro: divisão por zero não permitida.")
    return numerator / denominator

def multiplication(factor1, factor2):
    return factor1 * factor2
