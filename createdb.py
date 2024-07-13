import sqlite3

try:
    con = sqlite3.connect('cadastro_alunos.db')
    print('conexao com o banco de dados realizada com sucesso!')

except sqlite3.Error as e:
    print("Erro ao conectar com o banco de dados", e)

