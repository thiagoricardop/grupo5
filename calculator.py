# Calculator - Group 5
import sum
import subtract

import math


def power(base: float, exponent: float) -> float:
    return math.pow(base, exponent)

def division(numerator: float, denominator: float) -> float:
    if denominator == 0:
        raise ZeroDivisionError("Erro: divisão por zero não permitida.")
    return numerator / denominator

def sum (x, y):
    return x + y

def sub (x, y):
    return x - y





