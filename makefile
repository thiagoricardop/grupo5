# Makefile para Calculator - Group 5

.PHONY: all run test

# Alvo padrão
all: run

# Executa o programa
run:
	python3 main.py

# Executa testes (caso utilize unittest)
test:
	pytest test_calculator.py

