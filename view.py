# CRUD

import sqlite3

# Criando conexao
try:
    con = sqlite3.connect('cadastro_alunos.db')
    print("conexao com o banco de dados realizado com sucesso!")
except sqlite3.Error as e:
    print("Erro ao conectar com obanco de dados:", e)

# TABELA DE CURSOS -------------------------------------------------------

# Criar cursos (CREATE)
def criar_curso(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO cursos ( nome, duracoa, preco) VALUES(?,?,?)"
        cur.execute(query,i)

#criar_curso(['Python','2 semanas', 500])

# Ver todos os cursos (READE)
def ver_cursos():

    lista = []      # Lista para os itens 
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM cursos')
        linha = cur.fetchall()  # Busca todas as linhas do resultado da consulta e atribui a lista 

        for i in linha:
            lista.append(i)
        return lista
    
print(ver_cursos())

# Atualizar cursos (UPDATE)
def atualizaar_curso(i):
    with con:
        cur = con.cursor()
        query = "UPDATE cursos SET nome=?, duracoa=?, preco=? WHERE id=?"
        cur.execute(query,i)

l = ['Python','4 semanas', 400.00,1]
atualizaar_curso(l)


# Deletar os cursos (DELETE)
def deletar_curso(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM cursos WHERE id=?"
        cur.execute(query,i)

deletar_curso([1])


# TABELA DE TURMAS -------------------------------------------------------

# Criar turmas (CREATE)
def criar_turmas(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO turmas (nome, cursos_nome, data_inicio) VALUES (?,?,?)"
        cur.execute(query,i)


# Ler turmas (READE)
def ler_turmas():
        lista = []
        with con:
            cur = con.cursor()
            cur.execute('SELECT * FROM turmas')
            linha = cur.fetchall()

            for i in linha:
                lista.append(i)

        return lista


# Atualizar turmas (UPDATE)
def atualizar_turmas(i):
        with con:
            cur = con.cursor()
            query = "UPDATE turma SET nome=?, cursos_nome=?, data_inicio=? WHERE id=?"
            cur.execute(query,i)


# Deletar turmas (DELETE)
def deletar_turma(i):
    with con:
        cur = con.cursor()
        query = "DELETE  FROM turmas WHERE id=? "
        cur.execute(query,i)


# TABELA DE CURSOS -------------------------------------------------------

# Criar alunos (CREATE)
def criar_alunos(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO alunos(nome, emial, telefone, sexo, imagem, data_nascimento, cpf, turma_nome ) VALUES(?,?,?,?,?,?,?)"
        cur.execute(query, i)


# Ler alunos (READE)
def ler_alunos():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM alunos")
        cur.fetchall()

        for i in lista:
            lista.append(i)
    return lista


# Atualizar alunos (UPDATE)
def update_alunos(i):
    with con:
        cur = con.cursor()
        query = "UPDATE alunos SET nome=?, emial=?, telefone=?, sexo=?, imagem=?, data_nascimento=?, cpf=?, turma_nome=? WHERE id=? "
        cur.execute(query, i)


# Deletar alunos (DELETE)
def deletar_alunos(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM alunos WHERE id=?"
        cur.execute(query, i)

