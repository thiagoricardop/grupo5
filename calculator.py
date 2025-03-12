# Calculator - Group 5

import re
import math

def factorial(a):
    result = a
    for i in range(a-1, 0, -1):
        result *= i
    return result

def call_log(a):
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



# Processa fatorial aplicado a expressões entre parênteses, ex.: "(3+2)!" -> "factorial(<resultado_de_3+2>)"
def replace_paren_factorial(match):
    inner_expr = match.group(1)
    # Avalia a expressão interna recursivamente
    evaluated_inner = evaluate_expression(inner_expr)
    # Retorna a chamada da função factorial com o resultado da expressão interna
    return f'factorial({evaluated_inner})'

def replace_sqrt(match):
    inner_expr = match.group(1)
    # Chama evaluate_expression recursivamente para calcular a expressão interna
    evaluated_inner = evaluate_expression(inner_expr)
    # Retorna a chamada da função square_root com o resultado da expressão interna
    return f'square_root({evaluated_inner})'

def replace_log(match):
    base = match.group(1)  # Captura a base do log (se existir)
    inner_expr = match.group(2)  # Captura a expressão dentro do log()

    # Avalia a expressão dentro do log
    evaluated_value = evaluate_expression(inner_expr)

    # Se a base não for especificada, usa logaritmo natural
    if base is None:
        return f'log({evaluated_value})'
    else:
        return f'log({evaluated_value}, {base})'

def replace_exponentiation(match):
    base = match.group(1)   # Pode ser um número ou expressão entre parênteses
    exponent = match.group(2)  # Pode ser um número ou expressão entre parênteses
    # Retorna a chamada à função power com a base e o expoente sem os parênteses desnecessários
    return f'power({base}, {exponent})'

def treat_input(expression: str) -> str:
    """
    processa a entrada do usuário para a calculadora, identificando operadores e chamando as funções responsáveis.
    """
    expression = expression.replace(" ", "")  # Remove espaços
    
    expression = expression.replace(",", ".")
    # Verifica caracteres permitidos, incluindo números decimais
    if not re.match(r'^[0-9.()+\-*/^!a-zA-Z_]+$', expression):
        raise ValueError("Entrada inválida: caracteres não permitidos.")
    
    # Processa operador de fatorial (!) substituindo por factorial()
    expression = re.sub(r'(\d+)!', r'factorial(\1)', expression)

    expression = re.sub(r'v(\d+(\.\d+)?)', r'square_root(\1)', expression)
    
    # Enquanto houver ocorrências de v( ... ) sem parênteses aninhados
    while re.search(r'v\(([^()]+)\)', expression):
        expression = re.sub(r'v\(([^()]+)\)', replace_sqrt, expression)
    
    # O padrão abaixo captura casos em que base e/ou expoente são números ou expressões entre parênteses
    pattern_exp = r'((?:\([^()]*\)|\([^()]*\([^()]*\)[^()]*\)|\d+(?:\.\d+)?))\^((?:\([^()]*\)|\([^()]*\([^()]*\)[^()]*\)|\d+(?:\.\d+)?))'
    while re.search(pattern_exp, expression):
        expression = re.sub(pattern_exp, replace_exponentiation, expression)
    
    # Trata números científicos com 'e' (exemplo: 1e3 para 1000)
    expression = re.sub(r'(\d+(\.\d+)?)e(\d+)', r'\1*10**\3', expression)
    
    # Processa logaritmo (log) substituindo por log()
    pattern = r'(\d+)?log\(([^()]*(?:\([^()]*\)[^()]*)*)\)'
    expression = re.sub(pattern, replace_log, expression)

    return expression

def evaluate_expression(expression: str) -> float:
    """
    Avalia a expressão matemática sanitizada e chama as funções adequadas.
    """
    try:
        sanitized_expression = treat_input(expression)
        print(sanitized_expression)
        if '^' in sanitized_expression:
            sanitized_expression = treat_input(sanitized_expression)
            print ("entrei aqui")
        print(sanitized_expression)
        result = eval(sanitized_expression, {"math": math, "factorial": factorial, "power": power, "division": division, "multiplication": multiplication, "sum": sum, "sub": sub, "square_root": square_root, "log": math.log})
        return result
    except Exception as e:
        error_message = str(e)

        # Lista de substrings que indicam erro em uma função conhecida
        function_names = {"math", "factorial", "power", "division", "multiplication", 
                          "sum", "sub", "square_root", "log"}

        # Se o erro contiver uma dessas palavras-chave, tenta recalcular
        if any(func in error_message for func in function_names):
            return evaluate_expression(expression)  # Chama recursivamente
        
        # Se for outro tipo de erro, lança exceção normal
        raise ValueError(f"Erro ao processar a expressão: {e}")

if __name__ == "__main__":
    while(True):
        try:
            user_input = input("Digite uma expressão matemática: ")
            result = evaluate_expression(user_input)
            print("Resultado:", result)
            break
        except Exception as e:
            error_message = str(e)

            # Lista de substrings que indicam erro em uma função conhecida
            function_names = {"math", "factorial", "power", "division", "multiplication", 
                            "sum", "sub", "square_root", "log"}

            # Se o erro contiver uma dessas palavras-chave, tenta recalcular
            if any(func in error_message for func in function_names):
                evaluate_expression(user_input)  # Chama recursivamente
            
            # Se for outro tipo de erro, lança exceção normal
            raise ValueError(f"Erro ao processar a expressão: {e}")