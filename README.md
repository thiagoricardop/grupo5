# Calculadora Científica - Grupo 5

Uma calculadora científica de terminal que realiza operações básicas e avançadas, processando expressões matemáticas com suporte a prioridade de operadores.

## Funcionalidades

- **Adição**: `+`  
  Exemplo: `2 + 3 = 5`
- **Subtração**: `-`  
  Exemplo: `5 - 2 = 3`
- **Multiplicação**: `*`  
  Exemplo: `4 * 3 = 12`
- **Divisão**: `/`  
  Exemplo: `10 / 2 = 5`
- **Exponenciação**: `^`  
  Exemplo: `2^5 = 32`
- **Fatorial**: `!` (operador pós-fixado)  
  Exemplo: `5! = 120`
- **Raiz quadrada**: `v` (operador pré-fixado)  
  Exemplo: `v25 = 5`

## Uso

1. Ao iniciar o programa, o menu de operações será exibido.
2. Digite a expressão matemática desejada no formato suportado.
3. A calculadora processará a entrada e exibirá o resultado ou uma mensagem de erro, se aplicável.

**Prioridade dos operadores**:  
A calculadora segue a ordem PEMDAS (Parênteses, Expoentes, Multiplicação/Divisão, Adição/Subtração), com operadores adicionais como fatorial e raiz quadrada tendo prioridade adequada.

## Exemplos de Entrada/Saída

### Exemplo 1:
**Entrada:**  
Digite a expressão: 2+4-3+10*2

**Saída:**  
Resultado: 23

### Exemplo 2:
**Entrada:**  
Digite a expressão: x-d/r

**Saída:**  
Entrada inválida. Digite valores e operações válidas.

**Entrada corrigida:**  
Digite a expressão: 2^5

**Saída:**  
Resultado: 32
