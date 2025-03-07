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

<<<<<<< HEAD
def multiplication(factor1, factor2):
=======
def sum (x, y):
    return x + y

def sub (x, y):
    return x - y

def multiplication(factor1: float, factor2: float) -> float:
>>>>>>> 53123ebe4cb5d7ba85a6a261d13c901a17c3f372
    return factor1 * factor2

def square_root(number: float) -> float:
    if number < 0:
        raise ValueError("Erro: raiz quadrada de número negativo não permitida.")
    return math.sqrt(number)