from SGBD_IterMobi import *
import mysql.connector
from tkinter import *
from mysql.connector import Error
from threading import Timer

class Usuario:
    def __init__(self, nome, email, __senha, deficienciaVisual):
        self.nome = nome
        self.email = email
        self.__senha = __senha
        self.deficienciaVisual = deficienciaVisual
    
    def cadastrar(self):
        self.__senha = cripto(self.__senha)

        r = registrar(self.nome, self.email, self.__senha, self.deficienciaVisual)

        if r == 1:
            pass
        else:
            pass

class TelaCadastroLogin:
    def __init__(self, nome, email, __senha, deficienciaVisual):
        self.nome = nome
        self.email = email
        self.__senha = __senha
        self.deficienciaVisual = deficienciaVisual

        self.criaConta = Tk()
        self.criaConta.geometry("375x677")
        self.criaConta['bg'] = "#cfcbcb"
        self.criaConta.title("IterMobi")
        self.img1 = PhotoImage(file="triangulos_app.png")
        self.img2 = PhotoImage(file="logoProjGrande.png")

        self.lblLogo = Label(self.criaConta, image=self.img2, bg="#cfcbcb")        
        self.lblLogo.place(relx=0.25, rely=0.4)
        t = Timer(2, self.cadastrar)
        t.start()
        self.criaConta.mainloop()
 
    def cadastrar(self):
        self.lblLogo.destroy()
        
        self.lblTri = Label(self.criaConta, image=self.img1, bg="#cfcbcb")        
        self.lblTri.place(relx=0, rely=0)

        self.mainLbl = Label(self.criaConta, text="CRIE SUA CONTA", font="Helvetica 23 bold", bg = "#cfcbcb", fg = "#00226d")
        self.mainLbl.place(relx = 0.14,rely=0.1)
        self.lblNome = Label(self.criaConta, text="NOME", font="Arial 9", bg="#cfcbcb", fg = "#00226d")
        self.lblNome.place(relx = 0.14, rely= 0.2)
        self.lblEmail = Label(self.criaConta, text="EMAIL", font="Arial 9", bg="#cfcbcb", fg = "#00226d")
        self.lblEmail.place(relx = 0.14, rely= 0.35)
        self.lblSenha = Label(self.criaConta, text="SENHA", font="Arial 9", bg="#cfcbcb", fg = "#00226d")
        self.lblSenha.place(relx = 0.14, rely= 0.5)
        self.lblConfSenha = Label(self.criaConta, text="CONFIRMAR SENHA", font="Arial 9", bg="#cfcbcb", fg = "#00226d")
        self.lblConfSenha.place(relx = 0.14, rely= 0.65)

        self.entryNome = Entry(self.criaConta, relief = FLAT, font= "Helvetica 11")
        self.entryNome.place(width=270,height=50,relx = 0.14, rely= 0.25)
        self.entryEmail = Entry(self.criaConta, relief = FLAT, font= "Helvetica 11")
        self.entryEmail.place(width=270,height=50,relx = 0.14, rely= 0.40)
        self.entrySenha = Entry(self.criaConta, relief = FLAT, font= "Helvetica 11")
        self.entrySenha.place(width=270,height=50,relx = 0.14, rely= 0.55)
        self.entrySenha.config(show='*')
        self.entryConfSenha = Entry(self.criaConta, relief = FLAT, font= "Helvetica 11")
        self.entryConfSenha.place(width=270,height=50,relx = 0.14, rely= 0.70)
        self.entryConfSenha.config(show='*')
        self.botaoConfirma = Button(self.criaConta, text="ENTRAR", font="Arial 11 bold", bg="#00226d", fg = "#fff",relief = FLAT, activebackground="#6585cd", command=self.mostraSenha)
        self.botaoConfirma.place(width=270,height=50,relx = 0.14, rely= 0.80)
        self.btnCadastro = Label(self.criaConta, text="JÁ TEM CADASTRO? CLIQUE AQUI", font="Arial 10 bold", bg="#cfcbcb", fg = "#000", relief = FLAT)
        self.btnCadastro.place(width=270,height=50,relx = 0.14, rely= 0.90)
        self.btnCadastro.bind('<Button-1>', self.telaConectar)

        self.nomeUsuario = self.entryNome.get()
        self.emailUsuario = self.entryEmail.get()
        self.senha = self.entrySenha.get()

    def telaConectar(self, event):
        self.conectar = Tk()
        self.conectar.geometry("375x677")
        self.conectar['bg'] = "#cfcbcb"
        self.conectar.title("IterMobi")
        self.triangulosImg = PhotoImage(file="triangulos_app.png")
         
        self.lblTri = Label(self.conectar, image=self.triangulosImg)
        self.lblTri.pack()

        self.mainLbl = Label(self.conectar, text="CONECTAR", font="Helvetica 23 bold", bg = "#cfcbcb", fg = "#00226d")
        self.mainLbl.place(relx = 0.25,rely=0.1)
        self.lblEmail = Label(self.conectar, text="EMAIL", font="Arial 9", bg="#cfcbcb", fg = "black")
        self.lblEmail.place(relx = 0.14, rely= 0.32)
        self.lblSenha = Label(self.conectar, text="SENHA", font="Arial 9", bg="#cfcbcb", fg = "black")
        self.lblSenha.place(relx = 0.14, rely= 0.47)
        self.btnEsqSenha = Button(self.conectar, text="ESQUECI A SENHA", font="Arial 9 underline", bg="#cfcbcb", fg = "black", relief = FLAT)
        self.btnEsqSenha.place(relx = 0.14, rely= 0.6)
        self.lblConfSenha = Label(self.conectar, text="CADASTRE-SE PARA CONTINUAR", font="Arial 9", bg="#cfcbcb", fg = "black")
        self.lblConfSenha.place(relx = 0.22, rely= 0.2)

        self.entryEmail = Entry(self.conectar, relief = FLAT, font= "Helvetica 11")
        self.entryEmail.place(width=270,height=50,relx = 0.14, rely= 0.36)
        self.entrySenha = Entry(self.conectar, relief = FLAT, font= "Helvetica 11")
        self.entrySenha.place(width=270,height=50,relx = 0.14, rely= 0.5)

        self.botaoConfirma = Button(self.conectar, text="ENTRAR", font="Arial 11 bold", bg="#00226d", fg = "#fff",relief = FLAT, activebackground="#6585cd")
        self.botaoConfirma.place(width=270,height=50,relx = 0.14, rely= 0.80)
        self.conectar.mainloop()

    def telaEsqSenha(self):
        self.esqSenha = Tk()
        self.esqSenha.geometry("375x677")
        self.esqSenha['bg'] = "#cfcbcb"
        self.esqSenha.title("IterMobi")
        self.img = PhotoImage(file="triangulos_app.png")
        self.lblTri = Label(self.esqSenha, image=self.img,bg="#cfcbcb")
        self.lblTri.pack()

        self.texto = """ESQUECEU A
        SENHA?"""
        self.texto2 = """    ENVIAREMOS UM CÓDIGO DE
        CONFIRMAÇÃO PARA O EMAIL
        INFORMADO ABAIXO"""
        self.mainLbl = Label(self.esqSenha, text=self.texto, font="Helvetica 23 bold", bg = "#cfcbcb", fg = "#00226d")
        self.mainLbl.place(relx = 0.23,rely=0.1)
        self.infoLbl = Label(self.esqSenha, text = self.texto2, font="Helvetica 11",justify=LEFT, bg = "#cfcbcb", fg = "#000")
        self.infoLbl.place(relx = 0.12,rely=0.3)
        self.lblEmail = Label(self.esqSenha, text="DIGITE SEU EMAIL", font="Arial 11", bg="#cfcbcb", fg = "black")
        self.lblEmail.place(relx = 0.13, rely= 0.5)
        self.entryEmail = Entry(self.esqSenha, relief = FLAT, font= "Helvetica 11")
        self.entryEmail.place(width=270,height=50,relx = 0.13, rely= 0.56)
        self.botaoConfirma = Button(self.esqSenha, text="ENVIAR", font="Arial 11 bold", bg="#00226d", fg = "#fff",relief = FLAT, activebackground="#6585cd")
        self.botaoConfirma.place(width=270,height=50,relx = 0.14, rely= 0.80)
        self.esqSenha.mainloop()

    def telaEsqSenhaCodigo(self):
        self.esqSenhaCodigo = Tk()
        self.esqSenhaCodigo.geometry("375x677")
        self.esqSenhaCodigo['bg'] = "#cfcbcb"
        self.esqSenhaCodigo.title("IterMobi")
        self.img = PhotoImage(file="triangulos_app.png")
        self.lblTri = Label(self.esqSenhaCodigo, image=self.img, bg="#cfcbcb")
        self.lblTri.pack()

        self.texto = """ESQUECEU A
        SENHA?"""
        self.texto2 = """    CASO O CÓDIGO NÃO TENHA SIDO 
        ENVIADO, CLIQUE NO BOTÃO
        ABAIXO PARA REENVIÁ-LO"""
        self.mainLbl = Label(self.esqSenhaCodigo, text=self.texto, font="Helvetica 23 bold", bg = "#cfcbcb", fg = "#00226d")
        self.mainLbl.place(relx = 0.23,rely=0.1)
        self.infoLbl = Label(self.esqSenhaCodigo, text = self.texto2, font="Helvetica 11",justify=LEFT, bg = "#cfcbcb", fg = "#000")
        self.infoLbl.place(relx = 0.1,rely=0.5)
        self.lblCodigo = Label(self.esqSenhaCodigo, text="DIGITE O CÓDIGO DE CONFIRMAÇÃO", font="Arial 11", bg="#cfcbcb", fg = "black")
        self.lblCodigo.place(relx = 0.13, rely= 0.3)
        self.entryCodigo = Entry(self.esqSenhaCodigo, relief = FLAT, font= "Helvetica 11")
        self.entryCodigo.place(width=270,height=50,relx = 0.13, rely= 0.36)

        self.botaoReenvia = Button(self.esqSenhaCodigo, text="REENVIAR CÓDIGO", font="Arial 11 bold", bg="#6585cd", fg = "#fff",relief = FLAT, activebackground="#6585cd")
        self.botaoReenvia.place(width=230,height=40,relx = 0.2, rely= 0.64)
        
        self.botaoConfirma = Button(self.esqSenhaCodigo, text="ENVIAR", font="Arial 11 bold", bg="#00226d", fg = "#fff",relief = FLAT, activebackground="#6585cd")
        self.botaoConfirma.place(width=270,height=50,relx = 0.14, rely= 0.80)
        self.esqSenhaCodigo.mainloop()

    def telaEsqSenhaNova(self):
        self.esqSenhaNova = Tk()
        self.esqSenhaNova.geometry("375x677")
        self.esqSenhaNova['bg'] = "#cfcbcb"
        self.esqSenhaNova.title("IterMobi")
        self.img = PhotoImage(file="triangulos_app.png")
        self.lblTri = Label(self.esqSenhaNova, image=self.img,bg="#cfcbcb")
        self.lblTri.pack()

        self.texto = """ESQUECEU A
        SENHA?"""

        self.mainLbl = Label(self.esqSenhaNova, text=self.texto, font="Helvetica 23 bold", bg = "#cfcbcb", fg = "#00226d")
        self.mainLbl.place(relx = 0.24,rely=0.1)
        self.lblSenha = Label(self.esqSenhaNova, text="SENHA", font="Arial 11", bg="#cfcbcb", fg = "black")
        self.lblSenha.place(relx = 0.14, rely= 0.32)
        self.lblRepeteSenha = Label(self.esqSenhaNova, text="REPITA SUA NOVA SENHA", font="Arial 11", bg="#cfcbcb", fg = "black")
        self.lblRepeteSenha.place(relx = 0.14, rely= 0.47)

        self.entrySenha = Entry(self.esqSenhaNova, relief = FLAT, font= "Helvetica 11")
        self.entrySenha.place(width=270,height=50,relx = 0.14, rely= 0.36)
        self.entryRepeteSenha = Entry(self.esqSenhaNova, relief = FLAT, font= "Helvetica 11")
        self.entryRepeteSenha.place(width=270,height=50,relx = 0.14, rely= 0.5)
        
        self.botaoConfirma = Button(self.esqSenhaNova, text="CONFIRMAR", font="Arial 11 bold", bg="#00226d", fg = "#fff",relief = FLAT, activebackground="#6585cd")
        self.botaoConfirma.place(width=270,height=50,relx = 0.14, rely= 0.80)
        self.esqSenhaNova.mainloop()



#telaself.criaConta()
#telaConectar()
#telaEsqSenha()
#telaself.esqSenhaCodigo()
#telaself.esqSenhaNova()
#root.mainloop()
if __name__ == "__main__":
    TelaCadastroLogin('', '', '', '')
