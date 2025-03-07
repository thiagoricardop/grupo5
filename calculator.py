# Calculator - Group 5

import math

def power(base: float, exponent: float) -> float:
    return math.pow(base, exponent)

def division(numerator: float, denominator: float) -> float:
    if denominator == 0:
        raise ZeroDivisionError("Erro: divisão por zero não permitida.")
    return numerator / denominator

def multiplication(factor1: float, factor2: float) -> float:
    return factor1 * factor2

def square_root(number: float) -> float:
    if number < 0:
        raise ValueError("Erro: raiz quadrada de número negativo não permitida.")
    return math.sqrt(number)
