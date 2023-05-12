#<<<=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=>>>#
#IMPORTAR BANCO DE DADOS E CONECTAR
import sqlite3 as lite

con = lite.connect('dados.db')

#<<<=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=>>>#

#OPERACOES CRUD
#-------------- create --------------
def inserir_info(i):
    
    with con:
        cur = con.cursor()
        query = "INSERT INTO cadastro (nome, email, facebook, instagram, twitter, whatsapp, tiktok, idpasta) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        cur.execute(query, i)

#-------------- read --------------
def mostrar_info():
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM cadastro"
        cur.execute(query)

        informacao = cur.fetchall()

        for i in informacao:
            lista.append(i)
        return lista
    
#-------------- update --------------
def atualizar_info(i):

    with con:
        cur = con.cursor()
        query = "UPDATE cadastro SET nome=?, email=?, facebook=?, instagram=?, twitter=?, whatsapp=?, tiktok=?, idpasta=? WHERE id=?"
        cur.execute(query, i)

#-------------- delete --------------
def deletar_info(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM cadastro WHERE id=?"
        cur.execute(query, i)