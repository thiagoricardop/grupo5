# Calculator - Group 5

import re
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


def sum (x, y):
    return x + y

def sub (x, y):
    return x - y

def multiplication(factor1: float, factor2: float) -> float:
    return factor1 * factor2

def square_root(number: float) -> float:
    if number < 0:
        raise ValueError("Erro: raiz quadrada de número negativo não permitida.")
    return math.sqrt(number)

def treat_input(expression: str) -> str:
    """
    processa a entrada do usuário para a calculadora, identificando operadores e chamando as funções responsáveis.
    """
    expression = expression.replace(" ", "")  # Remove espaços
    
    expression = expression.replace(",", ".")
    # Verifica caracteres permitidos, incluindo números decimais
    if not re.match(r'^[0-9.()+\-*/^!velog]+$', expression):
        raise ValueError("Entrada inválida: caracteres não permitidos.")
    
    # Processa operador de fatorial (!) substituindo por factorial()
    expression = re.sub(r'(\d+)!', r'factorial(\1)', expression)
    
    # Processa operador de raiz quadrada (v) substituindo por square_root()
    expression = re.sub(r'v(\d+(\.\d+)?)', r'square_root(\1)', expression)
    
    # Processa operador de exponenciação (^) substituindo por power()
    expression = re.sub(r'(\d+(\.\d+)?)\^(\d+(\.\d+)?)', r'power(\1, \3)', expression)
    
    # Trata números científicos com 'e' (exemplo: 1e3 para 1000)
    expression = re.sub(r'(\d+(\.\d+)?)e(\d+)', r'\1*10**\3', expression)
    
    # Processa logaritmo (log) substituindo por log()
    expression = re.sub(r'log\((\d+(\.\d+)?)\)', r'log(\1)', expression)
    
    return expression

def evaluate_expression(expression: str) -> float:
    """
    Avalia a expressão matemática sanitizada e chama as funções adequadas.
    """
    try:
        sanitized_expression = treat_input(expression)
        result = eval(sanitized_expression, {"math": math, "factorial": factorial, "power": power, "division": division, "multiplication": multiplication, "sum": sum, "sub": sub, "square_root": square_root, "log": log})
        return result
    except Exception as e:
        raise ValueError(f"Erro ao processar a expressão: {e}")

if __name__ == "__main__":
    while(True):
        try:
            user_input = input("Digite uma expressão matemática: ")
            result = evaluate_expression(user_input)
            print("Resultado:", result)
            break
        except Exception as e:
            print("Erro: {} - tente novamente!".format(e))