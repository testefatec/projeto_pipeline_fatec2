Pipeline CI/CD com GitHub Actions e CodeQL — FATEC
📌 Sobre o Projeto

Este projeto foi desenvolvido como atividade prática da FATEC com o objetivo de demonstrar a utilização de uma pipeline CI/CD integrada ao GitHub Actions e à ferramenta de análise estática de segurança CodeQL.

O foco principal do trabalho foi validar como o CodeQL identifica vulnerabilidades em aplicações Python durante o processo automatizado de integração contínua.

Durante os testes, foram realizados três cenários diferentes:

✅ Execução da pipeline com código limpo e seguro
❌ Execução da pipeline com código vulnerável/malicioso
🔒 Execução da pipeline após a correção das vulnerabilidades
🛠️ Tecnologias Utilizadas
GitHub
GitHub Actions
CodeQL
Python
⚙️ Objetivo da Pipeline

A pipeline foi criada para:

Automatizar testes do projeto
Executar análise de segurança automaticamente
Detectar vulnerabilidades conhecidas no código
Validar boas práticas de desenvolvimento seguro
Demonstrar funcionamento do CodeQL em ambiente real
🔄 Fluxo da Pipeline
Push no GitHub
       ↓
GitHub Actions inicia a pipeline
       ↓
Instala dependências
       ↓
Executa testes automatizados
       ↓
Executa análise de segurança com CodeQL
       ↓
Pipeline aprovada ou bloqueada
🧪 Cenários Testados
✅ Teste 1 — Código Limpo

No primeiro teste, foi utilizado um código Python sem vulnerabilidades conhecidas.

Resultado:
Pipeline executada com sucesso
Nenhum alerta de segurança encontrado
CodeQL aprovou a análise
📷 Evidência do Teste
<img width="1080" height="274" alt="image" src="https://github.com/user-attachments/assets/21690c8f-1bed-4923-828b-2856be04ef23" />

❌ Teste 2 — Código Vulnerável

No segundo teste, foi inserido propositalmente um código vulnerável para verificar se o CodeQL seria capaz de detectar falhas de segurança.

O exemplo utilizado foi uma vulnerabilidade de SQL Injection (CWE-89).

Código Vulnerável Utilizado
import sqlite3

def buscar_usuario_vulneravel(username):
    # ❌ VULNERÁVEL: concatenação direta do input do usuário
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    query = f"SELECT * FROM usuarios WHERE username = '{username}'"

    # CodeQL detecta a vulnerabilidade aqui
    cursor.execute(query)

    return cursor.fetchall()
Problema de Segurança

O código acima permite que um usuário malicioso injete comandos SQL diretamente na consulta ao banco de dados.

Exemplo de ataque:

' OR '1'='1

Isso poderia permitir acesso indevido aos dados da aplicação.

Resultado:
Pipeline falhou durante a análise
CodeQL identificou a vulnerabilidade
Alerta gerado em:
Security
Code scanning alerts
📷 Evidência do Teste
<img width="1073" height="269" alt="image" src="https://github.com/user-attachments/assets/d2caa7dc-4355-48a1-9688-042865865a36" />

🔒 Teste 3 — Código Corrigido

Após a identificação da vulnerabilidade, o código foi corrigido utilizando consultas parametrizadas.

Código Corrigido
import sqlite3

def buscar_usuario_seguro(username):
    # ✅ SEGURO: uso de parâmetros preparados
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    query = "SELECT * FROM usuarios WHERE username = ?"

    cursor.execute(query, (username,))

    return cursor.fetchall()
Correção Aplicada

A utilização de parâmetros preparados impede que comandos SQL maliciosos sejam interpretados pelo banco de dados.

Resultado:
Pipeline executada com sucesso
Nenhuma vulnerabilidade detectada
CodeQL aprovou o código
📷 Evidência do Teste
<img width="1070" height="291" alt="image" src="https://github.com/user-attachments/assets/fe36d07a-b48a-4369-8bb5-9efad3931c7f" />

🔍 Outras Vulnerabilidades Estudadas

Além do SQL Injection, também foram analisados exemplos educacionais contendo:

Command Injection (CWE-78)
Path Traversal (CWE-22)
Hard-coded Credentials (CWE-798)
Weak Cryptography (CWE-327)
Insecure Deserialization (CWE-502)
Uso inseguro de eval() (CWE-94)
Geração insegura de números aleatórios (CWE-338)

Todos os exemplos foram utilizados apenas para fins acadêmicos e controlados.

📚 Aprendizados Obtidos

Durante o desenvolvimento do projeto, foi possível compreender:

Como funciona uma pipeline CI/CD
Como automatizar verificações de segurança
A importância da análise estática de código
Como o CodeQL detecta vulnerabilidades
Boas práticas de desenvolvimento seguro
Integração entre GitHub Actions e CodeQL
✅ Conclusão

O projeto demonstrou na prática como ferramentas de segurança podem ser integradas ao processo de desenvolvimento para identificar vulnerabilidades automaticamente antes da publicação do software.

A utilização do CodeQL junto ao GitHub Actions mostrou-se eficiente para reforçar a segurança da aplicação e aplicar conceitos de DevSecOps dentro da pipeline CI/CD.

👨‍💻 Autor

Projeto desenvolvido para fins acadêmicos na FATEC.
