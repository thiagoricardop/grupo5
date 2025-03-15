from calculator import *

if __name__ == "__main__":
    while True:
        try:
            user_input = input("Digite uma expressão matemática: ")
            result = evaluate_expression(user_input)
            print("Resultado:", result)
            break
        except Exception as e:
            print(e)
