# 🚀 Pipeline CI/CD com GitHub Actions e CodeQL

> **Projeto acadêmico — FATEC**  
> Demonstração prática de integração entre CI/CD, GitHub Actions e análise estática de segurança com CodeQL.

---

## 📌 Sobre o Projeto

Este projeto foi desenvolvido como atividade prática da FATEC com o objetivo de demonstrar a utilização de uma pipeline CI/CD integrada ao **GitHub Actions** e à ferramenta de análise estática de segurança **CodeQL**.

O foco principal foi validar como o CodeQL identifica vulnerabilidades em aplicações Python durante o processo automatizado de integração contínua.

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Função |
|---|---|
| ![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white) | Hospedagem e versionamento do código |
| ![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat&logo=githubactions&logoColor=white) | Automação da pipeline CI/CD |
| ![CodeQL](https://img.shields.io/badge/CodeQL-000000?style=flat&logo=github&logoColor=white) | Análise estática de segurança |
| ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) | Linguagem da aplicação analisada |

---

## ⚙️ Objetivo da Pipeline

A pipeline foi criada para:

- ✅ Automatizar testes do projeto
- 🔍 Executar análise de segurança automaticamente
- 🚨 Detectar vulnerabilidades conhecidas no código
- 📐 Validar boas práticas de desenvolvimento seguro
- 🧪 Demonstrar funcionamento do CodeQL em ambiente real

---

## 🔄 Fluxo da Pipeline

```
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
```

---

## 🧪 Cenários Testados

### ✅ Teste 1 — Código Limpo

- Código Python **sem vulnerabilidades** conhecidas
- **Resultado:** Pipeline executada com sucesso, nenhum alerta de segurança encontrado

📷 **Evidência:**

<img width="1080" height="274" alt="Pipeline com código limpo" src="https://github.com/user-attachments/assets/21690c8f-1bed-4923-828b-2856be04ef23" />

---

### ❌ Teste 2 — Código Vulnerável

Inserção proposital de vulnerabilidade **SQL Injection (CWE-89)**:

```python
import sqlite3
from flask import Flask, request

app = Flask(__name__)

# ❌ VULNERÁVEL: SQL Injection via Flask route
@app.route('/user/<username>')
def buscar_usuario_vulneravel(username):
    """SQL Injection vulnerability - user input directly in query"""
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # VULNERABILITY.: f-string with untrusted input
    query = f"SELECT * FROM usuarios WHERE username = '{username}'"
    cursor.execute(query)
    
    results = cursor.fetchall()
    conn.close()
    return str(results)

# ❌ VULNERÁVEL: SQL Injection via query parameter
@app.route('/delete')
def deletar_usuario_vulneravel():
    """SQL Injection via query parameter"""
    user_id = request.args.get('id')
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # VULNERABILITY: string concatenation with user input
    query = "DELETE FROM usuarios WHERE id = " + user_id
    cursor.execute(query)
    conn.commit()
    conn.close()
    return "Deleted"

# ❌ VULNERÁVEL: SQL Injection via POST data
@app.route('/update', methods=['POST'])
def atualizar_email_vulneravel():
    """SQL Injection via POST body"""
    email = request.form.get('email')
    user_id = request.form.get('id')
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # VULNERABILITY: % formatting with user input
    query = "UPDATE usuarios SET email = '%s' WHERE id = %s" % (email, user_id)
    cursor.execute(query)
    conn.commit()
    conn.close()
    return "Updated"

# ❌ VULNERÁVEL: SQL Injection via JSON
@app.route('/search', methods=['POST'])
def buscar_por_email():
    """SQL Injection via JSON body"""
    data = request.get_json()
    email = data.get('email')
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # VULNERABILITY: .format() with user input
    query = "SELECT * FROM usuarios WHERE email = '{}'".format(email)
    cursor.execute(query)
    
    results = cursor.fetchall()
    conn.close()
    return str(results)

if __name__ == '__main__':
    app.run(debug=True)
```

> ⚠️ **Problema:** Permite injeção de comandos SQL maliciosos.  
> **Resultado:** Pipeline falhou — CodeQL identificou a vulnerabilidade.

📷 **Evidência:**

<img width="1073" height="269" alt="Pipeline com código vulnerável" src="https://github.com/user-attachments/assets/d2caa7dc-4355-48a1-9688-042865865a36" />

> ⚠️ **ESSE CODÍGO FOI ENCONTRADO PARA TESTES DE VULNERABILIDADES NO REPOSITORIO DO DILLA** 

---

### 🔒 Teste 3 — Código Corrigido

Correção aplicada com **consultas parametrizadas**:

```python
import sqlite3

def buscar_usuario_seguro(username):
    # ✅ SEGURO: uso de parâmetros preparados
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    query = "SELECT * FROM usuarios WHERE username = ?"
    cursor.execute(query, (username,))
    return cursor.fetchall()
```

> **Resultado:** Pipeline executada com sucesso, nenhuma vulnerabilidade detectada.

📷 **Evidência:**

<img width="1070" height="291" alt="Pipeline com código corrigido" src="https://github.com/user-attachments/assets/fe36d07a-b48a-4369-8bb5-9efad3931c7f" />

---

## 🔍 Outras Vulnerabilidades Estudadas

| CWE | Tipo |
|---|---|
| CWE-78 | Command Injection |
| CWE-22 | Path Traversal |
| CWE-798 | Hard-coded Credentials |
| CWE-327 | Weak Cryptography |
| CWE-502 | Insecure Deserialization |
| CWE-94 | Uso inseguro de `eval()` |
| CWE-338 | Geração insegura de números aleatórios |

---

## 📚 Aprendizados Obtidos

- 🔁 Funcionamento de uma pipeline CI/CD
- 🤖 Automação de verificações de segurança
- 🔬 Importância da análise estática de código
- 🛡️ Detecção de vulnerabilidades com CodeQL
- 📖 Boas práticas de desenvolvimento seguro
- 🔗 Integração entre GitHub Actions e CodeQL

---

## ✅ Conclusão

O projeto demonstrou na prática como ferramentas de segurança podem ser integradas ao processo de desenvolvimento para **identificar vulnerabilidades automaticamente** antes da publicação.

A utilização do **CodeQL** junto ao **GitHub Actions** mostrou-se eficiente para reforçar a segurança da aplicação e aplicar conceitos de **DevSecOps** dentro da pipeline CI/CD.

---

## 👨‍💻 Autor

Projeto desenvolvido para fins acadêmicos na **FATEC**.
