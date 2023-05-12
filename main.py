from tkinter import *
from cgitb import text
from tkinter import font
from tkinter import ttk
from tkinter import messagebox

from colors import *
from view import *

#<<<=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=>>>#

#JANELA PRINCIPAL:
janela = Tk()
janela.title('Agenda Pessoal')
janela.geometry('1270x768')
janela.configure(background=co9)
#janela.resizable(width=False, height=False)

#<<<=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=>>>#



#<<<=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=>>>#
#FRAME CIMA ESQUERDA
frame_cima = Frame(janela, width=310, height=50, bg=co2, relief='flat')
frame_cima.grid(row=0, column=0)

app_nome = Label(frame_cima, text='Cadastro', anchor=NW, font=('Ivy 13 bold'), bg=co2, fg=co1)
app_nome.place(x=10, y=20)

#FRAME ESQUERDA-BAIXO
frame_baixo = Frame(janela, width=310, height=718, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

#FRAME DIREITA-TREEVIWER
frame_direita = Frame(janela, width=714, height=968, bg=t01, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

#<<<=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=>>>#
#VARIALVEL GLOBAL TREE eFUNCOES BOTOES
global tree

# ----------- Inserir -----------
def inserir():
    nome = e_nome.get()
    email = e_email.get()
    facebook = e_facebook.get()
    instagram = e_instagram.get()
    twitter = e_twitter.get()
    whatsapp = e_whatsapp.get()
    tiktok = e_tiktok.get()
    idpasta = e_idpasta.get()

    lista = [nome, email, facebook, instagram, twitter, whatsapp, tiktok, idpasta]

    if nome == '':
        messagebox.showerror('Erro','Nome obrigatorio!')
    else:
        inserir_info(lista)
        messagebox.showinfo('Sucesso','Dados salvos com sucesso!')
        e_nome.delete(0, 'end')
        e_email.delete(0, 'end')
        e_facebook.delete(0, 'end')
        e_instagram.delete(0, 'end')
        e_twitter.delete(0, 'end')
        e_whatsapp.delete(0, 'end')
        e_tiktok.delete(0, 'end')
        e_idpasta.delete(0, 'end')

    for widget in frame_direita.winfo_children():
        widget.destroy()

    mostrar()
# ----------- Atualizar -----------
def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor_id = tree_lista[0]

        e_nome.delete(0, 'end')
        e_email.delete(0, 'end')
        e_facebook.delete(0, 'end')
        e_instagram.delete(0, 'end')
        e_twitter.delete(0, 'end')
        e_whatsapp.delete(0, 'end')
        e_tiktok.delete(0, 'end')
        e_idpasta.delete(0, 'end')

        e_nome.insert(0, tree_lista[1])
        e_email.insert(0, tree_lista[2])
        e_facebook.insert(0, tree_lista[3])
        e_instagram.insert(0, tree_lista[4])
        e_twitter.insert(0, tree_lista[5])
        e_whatsapp.insert(0, tree_lista[6])
        e_tiktok.insert(0, tree_lista[7])
        e_idpasta.insert(0, tree_lista[8])

        def update():
            nome = e_nome.get()
            email = e_email.get()
            facebook = e_facebook.get()
            instagram = e_instagram.get()
            twitter = e_twitter.get()
            whatsapp = e_whatsapp.get()
            tiktok = e_tiktok.get()
            idpasta = e_idpasta.get()

            lista = [nome, email, facebook, instagram, twitter, whatsapp, tiktok, idpasta, valor_id]

            if nome == '':
                messagebox.showerror('Erro','Nome nao pode estar vazio!!!')
            else:
                atualizar_info(lista)
                messagebox.showinfo('Sucesso','Dados Alterados com sucesso!')
                e_nome.delete(0, 'end')
                e_email.delete(0, 'end')
                e_facebook.delete(0, 'end')
                e_instagram.delete(0, 'end')
                e_twitter.delete(0, 'end')
                e_whatsapp.delete(0, 'end')
                e_tiktok.delete(0, 'end')
                e_idpasta.delete(0, 'end')

            for widget in frame_direita.winfo_children():
                widget.destroy()

            mostrar()
                
        # Botao confirmar
        b_confirmar = Button(frame_baixo, command=update, text='Confirmar', width=10, font=('Ivy 9 bold'), bg=b05, fg=co0, relief='raised', overrelief='flat')
        b_confirmar.place(x=115, y=480)


    except IndexError:
        messagebox.showerror('Erro','Selecione um dos dados na tabela para continuar!!!')
# ----------- Deletar -----------
def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor_id = [tree_lista[0]]

        deletar_info(valor_id)
        messagebox.showinfo('Exclusao','Dados deletados com sucesso!')

        for widget in frame_direita.winfo_children():
            widget.destroy()

        mostrar()

    except IndexError:
        messagebox.showerror('Error','Dados nao deletados!')

#<<<=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=>>>#
# ----------- Nome -----------
l_nome = Label(frame_baixo, text='Nome: ', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_nome.place(x=10, y=20)

e_nome = Entry(frame_baixo, width=48, justify='left', relief='solid')
e_nome.place(x=10, y=40)
# ----------- Email -----------
l_email = Label(frame_baixo, text='Email: ', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_email.place(x=10, y=60)

e_email = Entry(frame_baixo, width=48, justify='left', relief='solid')
e_email.place(x=10, y=80)
# ----------- Facebook -----------
l_facebook = Label(frame_baixo, text='Facebook: ', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_facebook.place(x=10, y=100)

e_facebook = Entry(frame_baixo, width=48, justify='left', relief='solid')
e_facebook.place(x=10, y=120)
# ----------- Instagram -----------
l_instagram = Label(frame_baixo, text='Instagram: ', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_instagram.place(x=10, y=140)

e_instagram = Entry(frame_baixo, width=48, justify='left', relief='solid')
e_instagram.place(x=10, y=160)
# ----------- Twitter -----------
l_twitter = Label(frame_baixo, text='Twitter: ', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_twitter.place(x=10, y=180)

e_twitter = Entry(frame_baixo, width=48, justify='left', relief='solid')
e_twitter.place(x=10, y=200)
# ----------- whatsapp -----------
l_whatsapp = Label(frame_baixo, text='Whatsapp: ', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_whatsapp.place(x=10, y=220)

e_whatsapp = Entry(frame_baixo, width=48, justify='left', relief='solid')
e_whatsapp.place(x=10, y=240)
# ----------- tiktok -----------
l_tiktok = Label(frame_baixo, text='Tiktok: ', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_tiktok.place(x=10, y=260)

e_tiktok = Entry(frame_baixo, width=48, justify='left', relief='solid')
e_tiktok.place(x=10, y=280)
# ----------- idpasta -----------
l_idpasta = Label(frame_baixo, text='ID Pasta: ', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_idpasta.place(x=10, y=300)

e_idpasta = Entry(frame_baixo, width=48, justify='left', relief='solid')
e_idpasta.place(x=10, y=320)

#<<<=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=>>>#

#BOTOES C.R.U.D
# ----------- Create -----------
b_inserir = Button(frame_baixo, command=inserir, text='Adicionar', width=11, font=('Ivy 10 bold'), bg=b01, fg=co0, relief='raised', overrelief='flat')
b_inserir.place(x=10, y=450)
# ----------- Update -----------
b_atualizar = Button(frame_baixo, command=atualizar, text='Update', width=11, font=('Ivy 10 bold'), bg=b02, fg=co0, relief='raised', overrelief='flat')
b_atualizar.place(x=105, y=450)
# ----------- Delete -----------
b_deletar = Button(frame_baixo, command=deletar, text='Delete', width=11, font=('Ivy 10 bold'), bg=b03, fg=co0, relief='raised', overrelief='flat')
b_deletar.place(x=201, y=450)

#<<<=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=>>>#

#TABELA TREEVIWER DIREITA
# ----------- cabecalho -----------
def mostrar():
    global tree
    lista = mostrar_info()

    tabela_head = ['id', 'nome', 'email', 'facebook', 'instagram', 'twitter', 'whatsapp', 'tiktok', 'idpasta']

# ----------- criando tabela -----------
    tree = ttk.Treeview(frame_direita, selectmode="extended", columns=tabela_head, show="headings")
# ----------- scroll vertical -----------
    vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)
# ----------- scroll horizontal -----------
    hsb = ttk.Scrollbar(frame_direita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frame_direita.grid_rowconfigure(0, weight=12)


    hd=["center","center","center","center","center","center","center","center","center"]
    h=[30,150,150,100,100,100,100,100,100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in lista:
        tree.insert('', 'end', values=item)
# ----------- chamar funcao mostrar tablea -----------
mostrar()

#<<<=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=>>>#




#<<<=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=>>>#
janela.mainloop()