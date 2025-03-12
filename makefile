# Makefile para Calculator - Group 5

.PHONY: all run test clean

# Alvo padrão
all: run

# Executa o programa
run:
	python3 calculator.py

# Executa testes (caso utilize unittest)
test:
	python3 -m unittest discover

# Limpa arquivos compilados
clean:
	rm -rf __pycache__ *.pyc
