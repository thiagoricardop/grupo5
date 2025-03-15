import regex as re  # Use a biblioteca "regex" (pip install regex)
import math

def factorial(a):
    return math.factorial(a)

def log(a):
    return math.log10(a)

def power(base, exponent):
    return math.pow(base, exponent)

def division(numerator, denominator):
    if denominator == 0:
        raise ZeroDivisionError
    return numerator / denominator

def sum(x, y):
    return x + y

def sub(x, y):
    return x - y

def multiplication(factor1: float, factor2: float) -> float:
    return factor1 * factor2

def square_root(number: float) -> float:
    if number < 0:
        raise ValueError("Erro: raiz quadrada de número negativo não permitida.")
    return math.sqrt(number)

# Funções de substituição para cada operador:
def replace_factorial(match):
    expr = match.group("expr")
    evaluated_expr = evaluate_expression(expr)
    return f'factorial({evaluated_expr})'

def replace_sqrt(match):
    arg = match.group("arg")
    evaluated_arg = evaluate_expression(arg)
    return f'square_root({evaluated_arg})'

def replace_exponentiation(match):
    base = match.group("base")
    expo = match.group("expo")
    return f'power({base}, {expo})'

def replace_log_no_base(match):
    arg = match.group("arg")
    evaluated_arg = evaluate_expression(arg)
    return f'log({evaluated_arg})'

def treat_input(expression: str) -> str:
    expression = expression.replace(" ", "").replace(",", ".")
    
    # Verifica caracteres permitidos
    if not re.match(r'^[0-9.()+\-*/^!a-zA-Z_]+$', expression):
        raise ValueError("Entrada inválida: caracteres não permitidos.")
    
    # Padrão para parênteses balanceados (usa (?R) para recursividade)
    pattern_paren = r'\((?:[^()]+|(?R))*\)'
    
    # Processa fatorial: número, variável ou expressão entre parênteses seguida de "!"
    pattern_factorial = rf'(?P<expr>(?:{pattern_paren}|\d+(?:\.\d+)?|\w+)+)!'
    expression = re.sub(pattern_factorial, replace_factorial, expression, flags=re.VERBOSE)
    
    # Processa raiz: o símbolo "v" seguido de número, variável ou expressão entre parênteses
    pattern_sqrt = rf'v(?P<arg>(?:{pattern_paren}|\d+(?:\.\d+)?|\w+))'
    expression = re.sub(pattern_sqrt, replace_sqrt, expression, flags=re.VERBOSE)
    
    # Processa exponenciação: base ^ expoente
    pattern_exp = rf'(?P<base>(?:{pattern_paren}|\d+(?:\.\d+)?|\w+))\^(?P<expo>(?:{pattern_paren}|\d+(?:\.\d+)?|\w+))'
    while re.search(pattern_exp, expression, flags=re.VERBOSE):
        expression = re.sub(pattern_exp, replace_exponentiation, expression, flags=re.VERBOSE)
    
    # Trata números científicos com 'e' (ex: 1e3 vira 1*10**3)
    expression = re.sub(r'(\d+(?:\.\d+)?)e(\d+)', r'\1*10**\2', expression)
    
    # Processa log com base 10
    pattern_log = r'(?<![\d.])log\((?!.*?,)(?P<arg>[^)]+)\)'
    expression = re.sub(pattern_log, replace_log_no_base, expression)
    
    # **Solução:** Substitui "v(" por "square_root(", garantindo a conversão mesmo com fatorial no argumento.
    expression = expression.replace("v(", "square_root(")
    
    return expression

def evaluate_expression(expression: str) -> float:
    """
    Avalia a expressão matemática processada.
    """
    try:
        sanitized_expression = treat_input(expression)
        print("Expressão tratada:", sanitized_expression)
        result = eval(sanitized_expression, {
            
            "factorial": factorial,
            "power": power,
            "division": division,
            "multiplication": multiplication,
            "sum": sum,
            "sub": sub,
            "square_root": square_root,
            "log": log
        })
        return result
    except Exception as e:
        raise e
