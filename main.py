from tkinter import *

root = Tk()
root.geometry("375x677")
root['bg'] = "#cfcbcb"
root.title = "IterMobi"

def Usuarios():

    img = PhotoImage(file="triangulos_app.png")
    lblTri = Label(root, image=img,bg="#cfcbcb")
    lblTri.pack()

    mainLbl = Label(root, text="CRIE SUA CONTA", font="Helvetica 23 bold", bg = "#cfcbcb", fg = "#00226d")
    mainLbl.place(relx = 0.14,rely=0.1)
    lblNome = Label(root, text="NOME", font="Arial 9", bg="#cfcbcb", fg = "#00226d")
    lblNome.place(relx = 0.14, rely= 0.2)
    lblEmail = Label(root, text="EMAIL", font="Arial 9", bg="#cfcbcb", fg = "#00226d")
    lblEmail.place(relx = 0.14, rely= 0.35)
    lblSenha = Label(root, text="SENHA", font="Arial 9", bg="#cfcbcb", fg = "#00226d")
    lblSenha.place(relx = 0.14, rely= 0.5)
    lblConfSenha = Label(root, text="CONFIRMAR SENHA", font="Arial 9", bg="#cfcbcb", fg = "#00226d")
    lblConfSenha.place(relx = 0.14, rely= 0.65)

    entryNome = Entry(root, relief = FLAT)
    entryNome.place(width=270,height=50,relx = 0.14, rely= 0.25)
    entryEmail = Entry(root, relief = FLAT)
    entryEmail.place(width=270,height=50,relx = 0.14, rely= 0.40)
    entrySenha = Entry(root, relief = FLAT)
    entrySenha.place(width=270,height=50,relx = 0.14, rely= 0.55)
    entryConfSenha = Entry(root, relief = FLAT)
    entryConfSenha.place(width=270,height=50,relx = 0.14, rely= 0.70)

    botaoConfirma = Button(root, text="ENTRAR", font="Arial 11 bold", bg="#00226d", fg = "#fff",relief = FLAT, activebackground="#6585cd")
    botaoConfirma.place(width=270,height=50,relx = 0.14, rely= 0.80)

    btnCadastro = Button(root, text="JÁ TEM CADASTRO? CLIQUE AQUI", font="Arial 10 bold", bg="#cfcbcb", fg = "#000", relief = FLAT)
    btnCadastro.place(width=270,height=50,relx = 0.14, rely= 0.90)

def telaConectar():

    img = PhotoImage(file="triangulos_app.png")
    lblTri = Label(root, image=img,bg="#cfcbcb")
    lblTri.pack()

    mainLbl = Label(root, text="CONECTAR", font="Helvetica 23 bold", bg = "#cfcbcb", fg = "#00226d")
    mainLbl.place(relx = 0.25,rely=0.1)
    lblEmail = Label(root, text="EMAIL", font="Arial 9", bg="#cfcbcb", fg = "black")
    lblEmail.place(relx = 0.14, rely= 0.32)
    lblSenha = Label(root, text="SENHA", font="Arial 9", bg="#cfcbcb", fg = "black")
    lblSenha.place(relx = 0.14, rely= 0.47)
    btnEsqSenha = Button(root, text="ESQUECI A SENHA", font="Arial 9 underline", bg="#cfcbcb", fg = "black", relief = FLAT)
    btnEsqSenha.place(relx = 0.14, rely= 0.6)
    lblConfSenha = Label(root, text="CADASTRE-SE PARA CONTINUAR", font="Arial 9", bg="#cfcbcb", fg = "black")
    lblConfSenha.place(relx = 0.22, rely= 0.2)

    entryEmail = Entry(root, relief = FLAT)
    entryEmail.place(width=270,height=50,relx = 0.14, rely= 0.36)
    entrySenha = Entry(root, relief = FLAT)
    entrySenha.place(width=270,height=50,relx = 0.14, rely= 0.5)

    botaoConfirma = Button(root, text="ENTRAR", font="Arial 11 bold", bg="#00226d", fg = "#fff",relief = FLAT, activebackground="#6585cd")
    botaoConfirma.place(width=270,height=50,relx = 0.14, rely= 0.80)


def telaEsqSenha():
    img = PhotoImage(file="triangulos_app.png")
    lblTri = Label(root, image=img,bg="#cfcbcb")
    lblTri.pack()

    texto = """ESQUECEU A
    SENHA?"""

    mainLbl = Label(root, text=texto, font="Helvetica 23 bold", bg = "#cfcbcb", fg = "#00226d")
    mainLbl.place(relx = 0.24,rely=0.1)
    lblEmail = Label(root, text="EMAIL", font="Arial 9", bg="#cfcbcb", fg = "black")
    lblEmail.place(relx = 0.14, rely= 0.32)
    lblSenha = Label(root, text="SENHA", font="Arial 9", bg="#cfcbcb", fg = "black")
    lblSenha.place(relx = 0.14, rely= 0.47)
    lblNovaSenha = Label(root, text="REPITA SUA NOVA SENHA", font="Arial 9", bg="#cfcbcb", fg = "black", relief = FLAT)
    lblNovaSenha.place(relx = 0.14, rely= 0.6)
    lblConfSenha = Label(root, text="ADICIONE UMA NOVA SENHA", font="Arial 9", bg="#cfcbcb", fg = "black")
    lblConfSenha.place(relx = 0.27, rely= 0.25)

    entryEmail = Entry(root, relief = FLAT)
    entryEmail.place(width=270,height=50,relx = 0.14, rely= 0.36)
    entrySenha = Entry(root, relief = FLAT)
    entrySenha.place(width=270,height=50,relx = 0.14, rely= 0.5)
    entryNovaSenha = Entry(root, relief = FLAT)
    entryNovaSenha.place(width=270,height=50,relx = 0.14, rely= 0.64)

    botaoConfirma = Button(root, text="ENVIAR", font="Arial 11 bold", bg="#00226d", fg = "#fff",relief = FLAT, activebackground="#6585cd")
    botaoConfirma.place(width=270,height=50,relx = 0.14, rely= 0.80)

#telaCriaConta()
#telaConectar()
telaEsqSenha()
root.mainloop()
