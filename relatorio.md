# Relatório de Configuração do Projeto  <!-- (Título principal: nível 1) -->

## 1. Estratégia de Branching Utilizada  <!-- (Subtítulo: nível 2) -->
- Utilizamos o Git Flow.

## 2. Procedimentos de Build e CI/CD
### Build <!-- (Sub-subtítulo: nível 3) -->
- **Makefile** que configura, compila e executa o código principal ou o código de testes.
- Comandos disponíveis:
  1. **`make all`** – Executa o código e os testes.
  2. **`make run`** – Executa o código.
  3. **`make test`** – Executa os testes.

### Continuous Integration
- GitHub Actions para:
  - Verificação de sintaxe (lint).
  - Execução de `test_calculator.py` antes do pull request.

### Continuous Deployment
- Transferência remota para a máquina individual.
- Upload do projeto atualizado em uma branch específica.

## 3. Estrutura e Política de Testes
- Uso do framework **pytest** (`test_calculator.py`).
- Cada integrante deve rodar os testes antes de abrir um pull request.

## 4. Forma de Versionamento
- **Uso de releases** no formato `X.Y.Z`, onde:
  - **X (1.3.2 → "1")** – Nova versão principal.
  - **Y (1.3.2 → "3")** – Adição de funcionalidades.
  - **Z (1.3.2 → "2")** – Correções de bugs.

## 5. Gerenciamento de Issues
- Enumeração de issues do projeto (bugs e funcionalidades).
- Marcação como concluídas após aprovação e merge.

## 6. Lições Aprendidas
- Melhor integração da equipe no desenvolvimento.
- Aprendizado de ferramentas como GitHub Actions e testes automatizados.
- Uso eficiente de branches para organização do código.
  
