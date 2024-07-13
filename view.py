import sqlite3

# Criando conexao
try:
    con = sqlite3.connect('cadastro_alunos.db')
    print("conexao com o banco de dados realizado com sucesso!")
except sqlite3.Error as e:
    print("Erro ao conectar com obanco de dados:", e)

# TABELA DE CURSOS ------------------------------------

