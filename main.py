from tkinter import *

class Telas:
    def __init__(self, root):
        root = Tk()
        root.geometry("375x677")
        root['bg'] = "#cfcbcb"
        root.title("IterMobi")
        img = PhotoImage(file="triangulos_app.png")

    def telaCriaConta():

        lblTri = Label(root, image=img, bg="#cfcbcb")
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

        entryNome = Entry(root, relief = FLAT, font= "Helvetica 11")
        entryNome.place(width=270,height=50,relx = 0.14, rely= 0.25)
        entryEmail = Entry(root, relief = FLAT, font= "Helvetica 11")
        entryEmail.place(width=270,height=50,relx = 0.14, rely= 0.40)
        entrySenha = Entry(root, relief = FLAT, font= "Helvetica 11")
        entrySenha.place(width=270,height=50,relx = 0.14, rely= 0.55)
        entryConfSenha = Entry(root, relief = FLAT, font= "Helvetica 11")
        entryConfSenha.place(width=270,height=50,relx = 0.14, rely= 0.70)

        botaoConfirma = Button(root, text="ENTRAR", font="Arial 11 bold", bg="#00226d", fg = "#fff",relief = FLAT, activebackground="#6585cd")
        botaoConfirma.place(width=270,height=50,relx = 0.14, rely= 0.80)

        btnCadastro = Button(root, text="JÁ TEM CADASTRO? CLIQUE AQUI", font="Arial 10 bold", bg="#cfcbcb", fg = "#000", relief = FLAT)
        btnCadastro.place(width=270,height=50,relx = 0.14, rely= 0.90)

    def telaConectar():

         
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

        entryEmail = Entry(root, relief = FLAT, font= "Helvetica 11")
        entryEmail.place(width=270,height=50,relx = 0.14, rely= 0.36)
        entrySenha = Entry(root, relief = FLAT, font= "Helvetica 11")
        entrySenha.place(width=270,height=50,relx = 0.14, rely= 0.5)

        botaoConfirma = Button(root, text="ENTRAR", font="Arial 11 bold", bg="#00226d", fg = "#fff",relief = FLAT, activebackground="#6585cd")
        botaoConfirma.place(width=270,height=50,relx = 0.14, rely= 0.80)

    def telaEsqSenha():
         
        lblTri = Label(root, image=img,bg="#cfcbcb")
        lblTri.pack()

        texto = """ESQUECEU A
        SENHA?"""
        texto2 = """    ENVIAREMOS UM CÓDIGO DE
        CONFIRMAÇÃO PARA O EMAIL
        INFORMADO ABAIXO"""
        mainLbl = Label(root, text=texto, font="Helvetica 23 bold", bg = "#cfcbcb", fg = "#00226d")
        mainLbl.place(relx = 0.23,rely=0.1)
        infoLbl = Label(root, text = texto2, font="Helvetica 11",justify=LEFT, bg = "#cfcbcb", fg = "#000")
        infoLbl.place(relx = 0.12,rely=0.3)
        lblEmail = Label(root, text="DIGITE SEU EMAIL", font="Arial 11", bg="#cfcbcb", fg = "black")
        lblEmail.place(relx = 0.13, rely= 0.5)
        entryEmail = Entry(root, relief = FLAT, font= "Helvetica 11")
        entryEmail.place(width=270,height=50,relx = 0.13, rely= 0.56)
        botaoConfirma = Button(root, text="ENVIAR", font="Arial 11 bold", bg="#00226d", fg = "#fff",relief = FLAT, activebackground="#6585cd")
        botaoConfirma.place(width=270,height=50,relx = 0.14, rely= 0.80)

    def telaEsqSenhaCodigo():
         
        lblTri = Label(root, image=img, bg="#cfcbcb")
        lblTri.pack()

        texto = """ESQUECEU A
        SENHA?"""
        texto2 = """    CASO O CÓDIGO NÃO TENHA SIDO 
        ENVIADO, CLIQUE NO BOTÃO
        ABAIXO PARA REENVIALO"""
        mainLbl = Label(root, text=texto, font="Helvetica 23 bold", bg = "#cfcbcb", fg = "#00226d")
        mainLbl.place(relx = 0.23,rely=0.1)
        infoLbl = Label(root, text = texto2, font="Helvetica 11",justify=LEFT, bg = "#cfcbcb", fg = "#000")
        infoLbl.place(relx = 0.1,rely=0.5)
        lblCodigo = Label(root, text="DIGITE O CÓDIGO DE CONFIRMAÇÃO", font="Arial 11", bg="#cfcbcb", fg = "black")
        lblCodigo.place(relx = 0.13, rely= 0.3)
        entryCodigo = Entry(root, relief = FLAT, font= "Helvetica 11")
        entryCodigo.place(width=270,height=50,relx = 0.13, rely= 0.36)

        botaoReenvia = Button(root, text="REENVIAR CÓDIGO", font="Arial 11 bold", bg="#6585cd", fg = "#fff",relief = FLAT, activebackground="#6585cd")
        botaoReenvia.place(width=230,height=40,relx = 0.2, rely= 0.64)
        
        botaoConfirma = Button(root, text="ENVIAR", font="Arial 11 bold", bg="#00226d", fg = "#fff",relief = FLAT, activebackground="#6585cd")
        botaoConfirma.place(width=270,height=50,relx = 0.14, rely= 0.80)

    def telaEsqSenhaNova():
         
        lblTri = Label(root, image=img,bg="#cfcbcb")
        lblTri.pack()

        texto = """ESQUECEU A
        SENHA?"""

        mainLbl = Label(root, text=texto, font="Helvetica 23 bold", bg = "#cfcbcb", fg = "#00226d")
        mainLbl.place(relx = 0.24,rely=0.1)
        lblSenha = Label(root, text="SENHA", font="Arial 11", bg="#cfcbcb", fg = "black")
        lblSenha.place(relx = 0.14, rely= 0.32)
        lblRepeteSenha = Label(root, text="REPITA SUA NOVA SENHA", font="Arial 11", bg="#cfcbcb", fg = "black")
        lblRepeteSenha.place(relx = 0.14, rely= 0.47)

        entrySenha = Entry(root, relief = FLAT, font= "Helvetica 11")
        entrySenha.place(width=270,height=50,relx = 0.14, rely= 0.36)
        entryRepeteSenha = Entry(root, relief = FLAT, font= "Helvetica 11")
        entryRepeteSenha.place(width=270,height=50,relx = 0.14, rely= 0.5)
        
        botaoConfirma = Button(root, text="CONFIRMAR", font="Arial 11 bold", bg="#00226d", fg = "#fff",relief = FLAT, activebackground="#6585cd")
        botaoConfirma.place(width=270,height=50,relx = 0.14, rely= 0.80)

#telaCriaConta()
#telaConectar()
#telaEsqSenha()
#telaEsqSenhaCodigo()
#telaEsqSenhaNova()
root.mainloop()
