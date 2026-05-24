import sqlite3


def saudacao(nome: str) -> str:
    if not nome:
        return "Olá, visitante!"
    return f"Olá, {nome}!"


def calcular_media(notas: list) -> float:
    if not notas:
        return 0.0
    return sum(notas) / len(notas)


def validar_email(email: str) -> bool:
    if not email or '@' not in email:
        return False
    
    partes = email.split('@')
    if len(partes) != 2:
        return False
    
    usuario, dominio = partes
    return len(usuario) > 0 and len(dominio) > 0 and '.' in dominio


def main():
    print("=" * 50)
    print("🎓 Bem-vindo ao Sistema FATEC")
    print("=" * 50)
    
    print(saudacao("FATEC Santana de Parnaíba"))
    
    notas_aluno = [8.5, 9.0, 7.5, 8.0]
    media = calcular_media(notas_aluno)
    print(f"\n📊 Média do aluno: {media:.2f}")
    
    email_teste = "aluno@fatec.sp.gov.br"
    if validar_email(email_teste):
        print(f"✅ Email válido: {email_teste}")
    else:
        print(f"❌ Email inválido: {email_teste}")
    
    print("\n" + "=" * 50)
    print("✅ Aplicação executada com sucesso!")
    print("=" * 50)


if __name__ == "__main__":
    main()


def buscar_usuario_vulneravel(username):
    # ❌ VULNERÁVEL: concatenação direta do input do usuário
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    query = f"SELECT * FROM usuarios WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchall()
