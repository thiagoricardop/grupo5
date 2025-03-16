# Makefile para Calculator - Group 5


# Alvo padrão
all: run test

# Executa o programa
run:
	python3 main.py

# Executa testes (caso utilize unittest)
test:
	pytest test_calculator.py

