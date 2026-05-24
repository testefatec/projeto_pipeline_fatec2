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

    