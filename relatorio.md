# Relatório de configuração do projeto:

## 1. Estratégia de branching utilizada:
- Utilizamos o Git Flow.

## 2. Procedimentos de build e CI/CD:
- **Build**: arquivo makefile que configura, compila e executa o código principal ou o código de testes, segue os comandos do makefile:  
    1. **make all** (executa o código e o arquivo de testes);  
    2. **make run** (executa o código);  
    3. **make test** (executa o arquivo de testes);
- **Continuous Integration:** Git hub actions com verificação de sintaxe (lint). Execução do arquivo "test_calculator.py" e verificação do resultado dos testes unitarios automatizados antes da solicitação de pull request;
- **Continuous Deployment:** Trasferencia remota para a máquina individual e upload do projeto atualizado com uma branch especifica para aquela funcionalidade, usando pull request para revisão;

## 3. Estrutura e política de testes:
- Uso do framework pytest com o arquivo test_calculator.py;
- Cada integrante deve verificar se o teste é concluído corretamente antes de fazer um pull request;

## 4. Forma de versionamento:
- **Uso de releases**, com o seguinte modelo:  
    - Ex Release(1.3.2):  
         - **Primeiro numeral "1"**: Versão com um bloco de funcionalidades.  
         - **Segundo numeral "3"**: Adição de uma nova funcionalidade ou de um pequeno bloco de funcionalidades.  
         - **Terceiro numeral "2"**: Resolução de um bug ou de um pequeno numero de bugs.

## 5. Gerenciamento de issues:
- Primeiramente enumeramos as issues do projeto (bugs e funcionalidades) e marcamos como concluída através da configuração dos pull requests. Ou marcamos manualmente após a aprovação e merge do PR para o branch principal (main).

## 6. Lições aprendidas:
- Aprendemos como é feita a integração da equipe na implementação de um projeto computacional. Conhecemos ferramentas novas que ajudam bastante no desenvolvimento em equipe, uso de issues git actions e integração de testes unitários por exemplo;
- O uso de branches para cada funcionalidade ou correção de bugs também ajuda na organização, demanda um certo tempo para se acostumar com a estrutura mas após isso facilita com a manutenção do código;
