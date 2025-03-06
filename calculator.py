# Calculator - Group 5

import math

def power(base: float, exponent: float) -> float:
    return math.pow(base, exponent)

def division(numerator: float, denominator: float) -> float:
    if denominator == 0:
        raise ZeroDivisionError("Erro: divisão por zero não permitida.")
    return numerator / denominator

