import sqlite3 as lite

con = lite.connect('dados.db')

with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE cadastro(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT, facebook TEXT, instagram TEXT, twitter TEXT, whatsapp TEXT, tiktok TEXT, idpasta TEXT)")