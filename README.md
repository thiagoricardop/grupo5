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

**Uso de expressões numéricas dentro da operação de raíz quadrada e exponenciação**:  
Devem estar dentro de parênteses "()" para que a expressão seja resolvida antes da operação principal. Como por exemplo:

v(2\*5+6) -> v(10+6) -> v16 -> 4. **Resultado igual a 4**.  
v2\*5+6 -> 1.414\*5+6 -> 7.07 + 6 -> 13.07. **Resultado igual a 13.07**.

(2\*3 - 4)^(2+5) -> (6 - 4)^7 -> 2^7 -> 128. **Resultado igual a 128**.
2\*3 - 4^2 +5 -> 6 -16 + 5 -> -10 + 5 -> -5. **Resultado igual a -5**. 

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
