# main.py
import sqlite3


def saudacao(nome: str) -> str:
    """Retorna uma saudação segura."""
    if not isinstance(nome, str):
        raise TypeError("Nome deve ser uma string")
    return f"Olá, {nome}! Bem-vindo ao sistema."


def calcular_media(notas: list) -> float:
    """Calcula a média de uma lista de notas."""
    if not notas:
        raise ValueError("Lista de notas não pode ser vazia")
    return sum(notas) / len(notas)


if __name__ == "__main__":
    print(saudacao("Aluno FATEC"))
    print(f'Média: {calcular_media([8.5, 9.0, 7.5])}')

# Adicione ao final do main.py (temporariamente)


def buscar_usuario_vulneravel(user_id):
    """SQL INJECTION VULNERABILITY"""
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()
    # ⚠️ SQL INJECTION: CRITICAL - nunca concatenar input em SQL!
    sql_query = "SELECT * FROM users WHERE id = " + str(user_id)
    cursor.execute(sql_query)
    return cursor.fetchone()


def login_vulneravel(username, password):
    """SQL INJECTION in login"""
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()
    # ⚠️ SQL INJECTION: CRITICAL - usuário controla a query diretamente
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    return cursor.fetchone()


if __name__ == "__main__":
    # Simular entrada de usuário - CodeQL vai ver essa origem
    user_input = input("Digite o ID do usuário: ")
    resultado = buscar_usuario_vulneravel(user_input)
    print(resultado)
