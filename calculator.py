# Calculator - Group 5

import math

def log(a):
    return math.log(a)

def power(base: float, exponent: float) -> float:
    return math.pow(base, exponent)

def division(numerator: float, denominator: float) -> float:
    if denominator == 0:
        raise ZeroDivisionError("Erro: divisão por zero não permitida.")
    return numerator / denominator

def multiplication(factor1: float, factor2: float) -> float:
    return factor1 * factor2
