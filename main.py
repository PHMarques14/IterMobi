from tkinter import *

class Telas:
    def __init__(self):
        self.telaCriaConta()
        self.telaConectar()
        self.telaEsqSenha()
        self.telaEsqSenhaCodigo()
        self.telaEsqSenhaNova()
        self.telaLogo()

    def telaLogo(self):
        self.tela = Tk()
        self.tela.geometry("1280x720")
        self.tela['bg'] = "#cfcbcb"
        self.tela.title("IterMobi")
        img = PhotoImage(file="triangulos_appMotorista.png")

        lblTri = Label(self.tela, image=img, bg="#cfcbcb")
        lblTri.place(x=-2,y=-1)

        #TERMINAR CONFIGURAÇÃO DAS TELAS

    def telaCriaConta(self):
        self.criaConta = Tk()
        self.criaConta.geometry("375x677")
        self.criaConta['bg'] = "#cfcbcb"
        self.criaConta.title("IterMobi")
        img = PhotoImage(file="triangulos_app.png")

        lblTri = Label(self.criaConta, image=img, bg="#cfcbcb")
        lblTri.pack()

        mainLbl = Label(self.criaConta, text="CRIE SUA CONTA", font="Helvetica 23 bold", bg = "#cfcbcb", fg = "#00226d")
        mainLbl.place(relx = 0.14,rely=0.1)
        lblNome = Label(self.criaConta, text="NOME", font="Arial 9", bg="#cfcbcb", fg = "#00226d")
        lblNome.place(relx = 0.14, rely= 0.2)
        lblEmail = Label(self.criaConta, text="EMAIL", font="Arial 9", bg="#cfcbcb", fg = "#00226d")
        lblEmail.place(relx = 0.14, rely= 0.35)
        lblSenha = Label(self.criaConta, text="SENHA", font="Arial 9", bg="#cfcbcb", fg = "#00226d")
        lblSenha.place(relx = 0.14, rely= 0.5)
        lblConfSenha = Label(self.criaConta, text="CONFIRMAR SENHA", font="Arial 9", bg="#cfcbcb", fg = "#00226d")
        lblConfSenha.place(relx = 0.14, rely= 0.65)

        entryNome = Entry(self.criaConta, relief = FLAT, font= "Helvetica 11")
        entryNome.place(width=270,height=50,relx = 0.14, rely= 0.25)
        entryEmail = Entry(self.criaConta, relief = FLAT, font= "Helvetica 11")
        entryEmail.place(width=270,height=50,relx = 0.14, rely= 0.40)
        entrySenha = Entry(self.criaConta, relief = FLAT, font= "Helvetica 11")
        entrySenha.place(width=270,height=50,relx = 0.14, rely= 0.55)
        entryConfSenha = Entry(self.criaConta, relief = FLAT, font= "Helvetica 11")
        entryConfSenha.place(width=270,height=50,relx = 0.14, rely= 0.70)

        botaoConfirma = Button(self.criaConta, text="ENTRAR", font="Arial 11 bold", bg="#00226d", fg = "#fff",relief = FLAT, activebackground="#6585cd")
        botaoConfirma.place(width=270,height=50,relx = 0.14, rely= 0.80)

        btnCadastro = Button(self.criaConta, text="JÁ TEM CADASTRO? CLIQUE AQUI", font="Arial 10 bold", bg="#cfcbcb", fg = "#000", relief = FLAT)
        btnCadastro.place(width=270,height=50,relx = 0.14, rely= 0.90)
        self.criaConta.mainloop()

    def telaConectar(self):
        self.conectar = Tk()
        self.conectar.geometry("375x677")
        self.conectar['bg'] = "#cfcbcb"
        self.conectar.title("IterMobi")
        img = PhotoImage(file="triangulos_app.png")
         
        lblTri = Label(self.conectar, image=img,bg="#cfcbcb")
        lblTri.pack()

        mainLbl = Label(self.conectar, text="CONECTAR", font="Helvetica 23 bold", bg = "#cfcbcb", fg = "#00226d")
        mainLbl.place(relx = 0.25,rely=0.1)
        lblEmail = Label(self.conectar, text="EMAIL", font="Arial 9", bg="#cfcbcb", fg = "black")
        lblEmail.place(relx = 0.14, rely= 0.32)
        lblSenha = Label(self.conectar, text="SENHA", font="Arial 9", bg="#cfcbcb", fg = "black")
        lblSenha.place(relx = 0.14, rely= 0.47)
        btnEsqSenha = Button(self.conectar, text="ESQUECI A SENHA", font="Arial 9 underline", bg="#cfcbcb", fg = "black", relief = FLAT)
        btnEsqSenha.place(relx = 0.14, rely= 0.6)
        lblConfSenha = Label(self.conectar, text="CADASTRE-SE PARA CONTINUAR", font="Arial 9", bg="#cfcbcb", fg = "black")
        lblConfSenha.place(relx = 0.22, rely= 0.2)

        entryEmail = Entry(self.conectar, relief = FLAT, font= "Helvetica 11")
        entryEmail.place(width=270,height=50,relx = 0.14, rely= 0.36)
        entrySenha = Entry(self.conectar, relief = FLAT, font= "Helvetica 11")
        entrySenha.place(width=270,height=50,relx = 0.14, rely= 0.5)

        botaoConfirma = Button(self.conectar, text="ENTRAR", font="Arial 11 bold", bg="#00226d", fg = "#fff",relief = FLAT, activebackground="#6585cd")
        botaoConfirma.place(width=270,height=50,relx = 0.14, rely= 0.80)
        self.conectar.mainloop()

    def telaEsqSenha(self):
        self.esqSenha = Tk()
        self.esqSenha.geometry("375x677")
        self.esqSenha['bg'] = "#cfcbcb"
        self.esqSenha.title("IterMobi")
        img = PhotoImage(file="triangulos_app.png")
        lblTri = Label(self.esqSenha, image=img,bg="#cfcbcb")
        lblTri.pack()

        texto = """ESQUECEU A
        SENHA?"""
        texto2 = """    ENVIAREMOS UM CÓDIGO DE
        CONFIRMAÇÃO PARA O EMAIL
        INFORMADO ABAIXO"""
        mainLbl = Label(self.esqSenha, text=texto, font="Helvetica 23 bold", bg = "#cfcbcb", fg = "#00226d")
        mainLbl.place(relx = 0.23,rely=0.1)
        infoLbl = Label(self.esqSenha, text = texto2, font="Helvetica 11",justify=LEFT, bg = "#cfcbcb", fg = "#000")
        infoLbl.place(relx = 0.12,rely=0.3)
        lblEmail = Label(self.esqSenha, text="DIGITE SEU EMAIL", font="Arial 11", bg="#cfcbcb", fg = "black")
        lblEmail.place(relx = 0.13, rely= 0.5)
        entryEmail = Entry(self.esqSenha, relief = FLAT, font= "Helvetica 11")
        entryEmail.place(width=270,height=50,relx = 0.13, rely= 0.56)
        botaoConfirma = Button(self.esqSenha, text="ENVIAR", font="Arial 11 bold", bg="#00226d", fg = "#fff",relief = FLAT, activebackground="#6585cd")
        botaoConfirma.place(width=270,height=50,relx = 0.14, rely= 0.80)
        self.esqSenha.mainloop()

    def telaEsqSenhaCodigo(self):
        self.esqSenhaCodigo = Tk()
        self.esqSenhaCodigo.geometry("375x677")
        self.esqSenhaCodigo['bg'] = "#cfcbcb"
        self.esqSenhaCodigo.title("IterMobi")
        img = PhotoImage(file="triangulos_app.png")
        lblTri = Label(self.esqSenhaCodigo, image=img, bg="#cfcbcb")
        lblTri.pack()

        texto = """ESQUECEU A
        SENHA?"""
        texto2 = """    CASO O CÓDIGO NÃO TENHA SIDO 
        ENVIADO, CLIQUE NO BOTÃO
        ABAIXO PARA REENVIALO"""
        mainLbl = Label(self.esqSenhaCodigo, text=texto, font="Helvetica 23 bold", bg = "#cfcbcb", fg = "#00226d")
        mainLbl.place(relx = 0.23,rely=0.1)
        infoLbl = Label(self.esqSenhaCodigo, text = texto2, font="Helvetica 11",justify=LEFT, bg = "#cfcbcb", fg = "#000")
        infoLbl.place(relx = 0.1,rely=0.5)
        lblCodigo = Label(self.esqSenhaCodigo, text="DIGITE O CÓDIGO DE CONFIRMAÇÃO", font="Arial 11", bg="#cfcbcb", fg = "black")
        lblCodigo.place(relx = 0.13, rely= 0.3)
        entryCodigo = Entry(self.esqSenhaCodigo, relief = FLAT, font= "Helvetica 11")
        entryCodigo.place(width=270,height=50,relx = 0.13, rely= 0.36)

        botaoReenvia = Button(self.esqSenhaCodigo, text="REENVIAR CÓDIGO", font="Arial 11 bold", bg="#6585cd", fg = "#fff",relief = FLAT, activebackground="#6585cd")
        botaoReenvia.place(width=230,height=40,relx = 0.2, rely= 0.64)
        
        botaoConfirma = Button(self.esqSenhaCodigo, text="ENVIAR", font="Arial 11 bold", bg="#00226d", fg = "#fff",relief = FLAT, activebackground="#6585cd")
        botaoConfirma.place(width=270,height=50,relx = 0.14, rely= 0.80)
        self.esqSenhaCodigo.mainloop()

    def telaEsqSenhaNova(self):
        self.esqSenhaNova = Tk()
        self.esqSenhaNova.geometry("375x677")
        self.esqSenhaNova['bg'] = "#cfcbcb"
        self.esqSenhaNova.title("IterMobi")
        img = PhotoImage(file="triangulos_app.png")
        lblTri = Label(self.esqSenhaNova, image=img,bg="#cfcbcb")
        lblTri.pack()

        texto = """ESQUECEU A
        SENHA?"""

        mainLbl = Label(self.esqSenhaNova, text=texto, font="Helvetica 23 bold", bg = "#cfcbcb", fg = "#00226d")
        mainLbl.place(relx = 0.24,rely=0.1)
        lblSenha = Label(self.esqSenhaNova, text="SENHA", font="Arial 11", bg="#cfcbcb", fg = "black")
        lblSenha.place(relx = 0.14, rely= 0.32)
        lblRepeteSenha = Label(self.esqSenhaNova, text="REPITA SUA NOVA SENHA", font="Arial 11", bg="#cfcbcb", fg = "black")
        lblRepeteSenha.place(relx = 0.14, rely= 0.47)

        entrySenha = Entry(self.esqSenhaNova, relief = FLAT, font= "Helvetica 11")
        entrySenha.place(width=270,height=50,relx = 0.14, rely= 0.36)
        entryRepeteSenha = Entry(self.esqSenhaNova, relief = FLAT, font= "Helvetica 11")
        entryRepeteSenha.place(width=270,height=50,relx = 0.14, rely= 0.5)
        
        botaoConfirma = Button(self.esqSenhaNova, text="CONFIRMAR", font="Arial 11 bold", bg="#00226d", fg = "#fff",relief = FLAT, activebackground="#6585cd")
        botaoConfirma.place(width=270,height=50,relx = 0.14, rely= 0.80)
        self.esqSenhaNova.mainloop()


#telaself.criaConta()
#telaConectar()
#telaEsqSenha()
#telaself.esqSenhaCodigo()
#telaself.esqSenhaNova()
#root.mainloop()
if __name__ == "__main__":
    Telas()
