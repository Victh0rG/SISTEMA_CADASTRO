import sqlite3

try:
    #cria banco de dados
    con = sqlite3.connect('cadastro_alunos.db')
    print('conexao com o banco de dados realizada com sucesso!')

except sqlite3.Error as e:
    print("Erro ao conectar com o banco de dados", e)

#criando tabela para cursos
try:
    with con:
        #criando variavel para instrucoes SQL
        cur = con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS cursos(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    duracoa TEXT,
                    preco REAL)
            """)
        
        print("tabela cursos criado com sucesso!")

except sqlite3.Error as e:
    print("Erro ao criar a tabela cursos", e)