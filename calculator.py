import regex as re  # Use a biblioteca "regex" (pip install regex)
import math

def factorial(a):
    a = round(float(a))
    a = int(a)
    result = a
    for i in range(a - 1, 0, -1):
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

def replace_log_with_base(match):
    base = match.group("base")
    arg = match.group("arg")
    evaluated_arg = evaluate_expression(arg)
    return f'log({evaluated_arg}, {base})'

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
    
    # Processa log com base: ex: "3log(20*2-13)"
    pattern_log_with_base = r'(?<![\d.])(?P<base>\d+)log\((?P<arg>[^)]+)\)'
    expression = re.sub(pattern_log_with_base, replace_log_with_base, expression)
    
    # Processa log sem base: não casa se houver vírgula no argumento
    pattern_log_no_base = r'(?<![\d.])log\((?!.*?,)(?P<arg>[^)]+)\)'
    expression = re.sub(pattern_log_no_base, replace_log_no_base, expression)
    
    # Etapa final: se ainda houver '^', substitui por '**'
    if '^' in expression:
        expression = expression.replace('^', '**')
    
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
            "math": math,
            "factorial": factorial,
            "power": power,
            "division": division,
            "multiplication": multiplication,
            "sum": sum,
            "sub": sub,
            "square_root": square_root,
            "log": math.log
        })
        return result
    except Exception as e:
        raise ValueError(f"Erro ao processar a expressão: {e}")

if __name__ == "__main__":
    while True:
        try:
            user_input = input("Digite uma expressão matemática: ")
            result = evaluate_expression(user_input)
            print("Resultado:", result)
            break
        except Exception as e:
            print(e)
