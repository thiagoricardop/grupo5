# Relatório de configuração do projeto:

## 1. Estratégia de branching utilizada:
- Utilizamos o Git Flow (mencionado no anunciado da atividade). 

## 2. Procedimentos de build e CI/CD:
- **Build**: Utilizamos o arquivo makefile para compilar e executar o código principal e/ou o código de testes, segue os comandos do makefile:  
    - **make all** (executa o código principal e o arquivo de testes);  
    - **make run** (executa apenas o código principal);  
    - **make test** (executa apenas o arquivo de testes);
- **Continuous Integration:**  
      - Uso do Github actions para monitorar os pull requests, com execução dos arquivos "docker-build.yml", "label_issues_automation.yml" e "pytest_automation.yml".   
- **Continuous Deployment:**  
      - Transferência remota para a máquina individual e upload do projeto atualizado com uma branch especifica para aquela funcionalidade, usando pull request para revisão;

## 3. Estrutura e política de testes:
- Uso do framework pytest com o arquivo test_calculator.py;
- O Github faz a verificação do pull request atraves dos arquivos da pasta .github/workflows

## 4. Forma de versionamento:
- **Uso de releases**, com o seguinte modelo:  
    - Ex Release(1.3.2):  
         - **Primeiro numeral "1"**: Versão com um bloco de funcionalidades.  
         - **Segundo numeral "3"**: Adição de uma nova funcionalidade ou de um pequeno bloco de funcionalidades.  
         - **Terceiro numeral "2"**: Resolução de um bug ou de um pequeno numero de bugs.

## 5. Gerenciamento de issues:
- Primeiramente enumeramos as issues do projeto (bugs e funcionalidades) e marcamos como concluída através da configuração dos pull requests. Ou marcamos manualmente após a aprovação e merge do PR para o branch principal (main).

## 6. Lições aprendidas:
- Aprendemos como é feita a integração da equipe na implementação de um projeto computacional. Conhecemos ferramentas novas que ajudam bastante no desenvolvimento em equipe, como por exemplo o uso de issues, git actions e integração de testes unitários;
- O uso de branches para cada funcionalidade ou correção de bugs também ajudam na organização, demanda um certo tempo para se acostumar com a estrutura mas após isso facilita a manutenção do código;
