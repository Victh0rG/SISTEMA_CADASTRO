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

        #TABELA PARA CURSOS
        cur.execute(""" CREATE TABLE IF NOT EXISTS cursos(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    duracoa TEXT,
                    preco REAL)
            """)
        
        print("tabela cursos criado com sucesso!")

except sqlite3.Error as e:
    print("Erro ao criar a tabela cursos", e)

# CRIANDO TABELA PARA TURMAS
try:
    with con:
        cur = con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS turmas(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    curso_nome TEXT,
                    data_inicio DATE,
                    FOREIGN KEY (curso_nome) REFERENCES cursos (nome) ON UPDATE CASCADE ON DELETE CASCADE)
            """)

    print("Tabela de turmas criada com sucesso!")

except sqlite3.Error as e:
    print("Erro ao criar a tablea cursos", e)


# CRIANDO TABELA PARA ALUNO
try:
    with con:
        cur = con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS alunos(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    emial TEXT,
                    telefone TEXT,
                    sexo TEXT,
                    imagem TEXT,
                    data_nascimento DATE,
                    cpf TEXT,
                    turma_nome TEXT,
                    FOREIGN KEY(turma_nome) REFERENCES cursos (nome) ON DELETE CASCADE) 
            """)

    print("Tabela alunos criada com sucesso!")

except sqlite3.Error as e:
    print("Erro ao criar a tabela Alunos", e)