from SGBD_IterMobi import *
import mysql.connector
from tkinter import *
from threading import Timer

class Usuario:
    def __init__(self, nome, email, __senha):
        self.nome = nome
        self.email = email
        self.__senha = __senha
    
    def cadastrar(self):
        self.__senha = cripto(self.__senha)

        r = registrar(self.nome, self.email, self.__senha)

        if r == 1:
            pass
        else:
            pass

class CadastroLogin:
    def __init__(self, nome, email, __senha):
        self.nome = nome
        self.email = email
        self.__senha = __senha

        self.tela = Tk()
        self.tela.geometry("375x677")
        self.tela['bg'] = "#cfcbcb"
        self.tela.title("IterMobi")
        self.img1 = PhotoImage(file="triangulos_app.png")
        self.img2 = PhotoImage(file="logoProjGrande.png")

        self.lblLogo = Label(self.tela, image=self.img2, bg="#cfcbcb")        
        self.lblLogo.place(relx=0.25, rely=0.4)
        t = Timer(2, lambda: self.cadastro(0))
        t.start()
        self.tela.mainloop()
 
    def cadastro(self, event):
        '''Tela de cadastro do aplicativo'''
        self.lblLogo.destroy()
        try:
            self.btnEsqSenha.destroy()
            self.btnConfirma.destroy()
            self.btnCadastroLogin.destroy()
            self.mainLbl.destroy()
            self.lblEmail.destroy()
            self.lblSenha.destroy()
            self.entryEmail.destroy()
            self.entrySenha.destroy()

        except:
            pass
        
        self.lblTri = Label(self.tela, image=self.img1, bg="#cfcbcb")        
        self.lblTri.place(relx=0, rely=0)

        self.mainLbl = Label(self.tela, text="CRIE SUA CONTA", font="Helvetica 23 bold", bg = "#cfcbcb", fg = "#00226d")
        self.mainLbl.place(relx = 0.14,rely=0.1)
        self.lblNome = Label(self.tela, text="NOME", font="Arial 9", bg="#cfcbcb", fg = "#00226d")
        self.lblNome.place(relx = 0.14, rely= 0.2)
        self.lblEmail = Label(self.tela, text="EMAIL", font="Arial 9", bg="#cfcbcb", fg = "#00226d")
        self.lblEmail.place(relx = 0.14, rely= 0.35)
        self.lblSenha = Label(self.tela, text="SENHA", font="Arial 9", bg="#cfcbcb", fg = "#00226d")
        self.lblSenha.place(relx = 0.14, rely= 0.5)
        self.lblConfSenha = Label(self.tela, text="CONFIRMAR SENHA", font="Arial 9", bg="#cfcbcb", fg = "#00226d")
        self.lblConfSenha.place(relx = 0.14, rely= 0.65)

        self.entryNome = Entry(self.tela, relief = FLAT, font= "Helvetica 14")
        self.entryNome.place(width=270,height=50,relx = 0.14, rely= 0.25)
        self.entryEmail = Entry(self.tela, relief = FLAT, font= "Helvetica 14")
        self.entryEmail.place(width=270,height=50,relx = 0.14, rely= 0.40)
        self.entrySenha = Entry(self.tela, relief = FLAT, font= "Helvetica 14")
        self.entrySenha.place(width=270,height=50,relx = 0.14, rely= 0.55)
        self.entrySenha.config(show='*')
        self.entryConfSenha = Entry(self.tela, relief = FLAT, font= "Helvetica 14")
        self.entryConfSenha.place(width=270,height=50,relx = 0.14, rely= 0.70)
        self.entryConfSenha.config(show='*')
        self.btnConfirma = Button(self.tela, text="ENTRAR", font="Arial 11 bold", bg="#00226d", fg = "#fff",relief = FLAT, activebackground="#6585cd")
        self.btnConfirma.place(width=270,height=50,relx = 0.14, rely= 0.80)
        self.btnConfirma.bind('<Return>', self)
        self.btnCadastroLogin = Label(self.tela, text="JÁ TEM CADASTRO? CLIQUE AQUI", font="Arial 9 underline", bg="#cfcbcb", fg = "#000", relief = FLAT)
        self.btnCadastroLogin.place(relx = 0.23, rely= 0.90)
        self.btnCadastroLogin.bind('<Button-1>', self.login)

        self.nomeUsuario = self.entryNome.get()
        self.emailUsuario = self.entryEmail.get()
        self.senha = self.entrySenha.get()

    def login(self, event):
        '''Tela de login do aplicativo'''
        self.lblNome.destroy()
        self.entryNome.destroy()
        self.lblConfSenha.destroy()
        self.entryConfSenha.destroy()

        self.mainLbl.configure(text="CONECTAR", font="Helvetica 23 bold", bg = "#cfcbcb", fg = "#00226d")
        self.mainLbl.place(relx = 0.25,rely=0.1)
        self.lblEmail.configure(text="EMAIL", font="Arial 9", bg="#cfcbcb", fg = "black")
        self.lblEmail.place(relx = 0.14, rely= 0.32)
        self.lblSenha.configure(text="SENHA", font="Arial 9", bg="#cfcbcb", fg = "black")
        self.lblSenha.place(relx = 0.14, rely= 0.47)
        self.btnEsqSenha = Label(self.tela, text="ESQUECI A SENHA", font="Arial 9 underline", bg="#cfcbcb", fg = "black", relief = FLAT)
        self.btnEsqSenha.place(relx = 0.14, rely= 0.6)
        self.btnEsqSenha.bind('<Button-1>', self.esqueceuSenha)
        self.btnCadastroLogin.configure(text="CADASTRE-SE PARA CONTINUAR", font="Arial 9 underline", bg="#cfcbcb", fg = "black")
        self.btnCadastroLogin.place(relx = 0.14, rely= 0.8)
        self.btnCadastroLogin.bind('<Button-1>', self.cadastro)

        self.entryEmail.configure(relief = FLAT, font= "Helvetica 14")
        self.entryEmail.place(width=270,height=50,relx = 0.14, rely= 0.36)
        self.entrySenha.configure(relief = FLAT, font= "Helvetica 14")
        self.entrySenha.place(width=270,height=50,relx = 0.14, rely= 0.5)

        self.btnConfirma.configure(text="ENTRAR", font="Arial 11 bold", bg="#00226d", fg = "#fff",relief = FLAT, activebackground="#6585cd")
        self.btnConfirma.place(width=270,height=50,relx = 0.14, rely= 0.7)
    def esqueceuSenha(self, event):
        self.btnEsqSenha.destroy()
        self.entrySenha.destroy()
        self.lblSenha.destroy()
        self.btnCadastroLogin.destroy()

        self.texto = """ESQUECEU A
        SENHA?"""
        self.texto2 = """
ENVIAREMOS UM CÓDIGO DE CONFIRMAÇÃO
PARA O EMAIL INFORMADO ABAIXO"""
        self.mainLbl.configure(text=self.texto, font="Helvetica 23 bold", bg = "#cfcbcb", fg = "#00226d")
        self.mainLbl.place(relx = 0.23,rely=0.1)
        self.infoLbl= Label(self.tela, text = self.texto2, font="Helvetica 11", justify=LEFT, bg = "#cfcbcb", fg = "#000")
        self.infoLbl.place(relx = 0.07,rely=0.3)
        self.lblEmail.configure(text="DIGITE SEU EMAIL", font="Arial 11", bg="#cfcbcb", fg = "black")
        self.lblEmail.place(relx = 0.13, rely= 0.5)
        self.entryEmail.configure(relief = FLAT, font= "Helvetica 11")
        self.entryEmail.place(width=270,height=50,relx = 0.13, rely= 0.56)
        self.btnConfirma.configure(text="ENVIAR", font="Arial 11 bold", bg="#00226d", fg = "#fff",relief = FLAT, activebackground="#6585cd")
        self.btnConfirma.place(width=270,height=50,relx = 0.14, rely= 0.80)
        self.btnConfirma.bind('<Return>', self.codigo)
        self.btnConfirma.bind('<Button-1>', self.codigo)

    def codigo(self, event):
        self.lblEmail.destroy()
        self.entryEmail.destroy()
        '''Enivia um código ao e-mail inserido pelo usuário'''

        self.texto = """ESQUECEU A
        SENHA?"""
        self.texto2 = """CASO O CÓDIGO NÃO TENHA SIDO 
        ENVIADO, CLIQUE NO BOTÃO
        ABAIXO PARA REENVIÁ-LO"""
        self.mainLbl.configure(text=self.texto, font="Helvetica 23 bold", bg = "#cfcbcb", fg = "#00226d")
        self.mainLbl.place(relx = 0.23,rely=0.1)
        self.infoLbl.configure(text = self.texto2, font="Helvetica 11",justify=LEFT, bg = "#cfcbcb", fg = "#000")
        self.infoLbl.place(relx = 0.1,rely=0.5)
        self.lblCodigo = Label(self.tela, text="DIGITE O CÓDIGO DE CONFIRMAÇÃO", font="Arial 11", bg="#cfcbcb", fg = "black")
        self.lblCodigo.place(relx = 0.13, rely= 0.3)
        self.entryCodigo = Entry(self.tela, relief = FLAT, font= "Helvetica 11")
        self.entryCodigo.place(width=270,height=50,relx = 0.13, rely= 0.36)

        self.botaoReenvia = Button(self.tela, text="REENVIAR CÓDIGO", font="Arial 11 bold", bg="#6585cd", fg = "#fff",relief = FLAT, activebackground="#6585cd")
        self.botaoReenvia.place(width=230,height=40,relx = 0.2, rely= 0.64)

    def alterar(self):
        '''Altera a senha antiga da conta do usuário e insere uma nova senha ao banco de dados'''

        self.texto = """ESQUECEU A
        SENHA?"""

        self.mainLbl = Label(self.tela, text=self.texto, font="Helvetica 23 bold", bg = "#cfcbcb", fg = "#00226d")
        self.mainLbl.place(relx = 0.24,rely=0.1)
        self.lblSenha = Label(self.tela, text="SENHA", font="Arial 11", bg="#cfcbcb", fg = "black")
        self.lblSenha.place(relx = 0.14, rely= 0.32)
        self.lblRepeteSenha = Label(self.tela, text="REPITA SUA NOVA SENHA", font="Arial 11", bg="#cfcbcb", fg = "black")
        self.lblRepeteSenha.place(relx = 0.14, rely= 0.47)

        self.entrySenha = Entry(self.tela, relief = FLAT, font= "Helvetica 11")
        self.entrySenha.place(width=270,height=50,relx = 0.14, rely= 0.36)
        self.entryRepeteSenha = Entry(self.tela, relief = FLAT, font= "Helvetica 11")
        self.entryRepeteSenha.place(width=270,height=50,relx = 0.14, rely= 0.5)
        
        self.btnConfirma = Button(self.tela, text="CONFIRMAR", font="Arial 11 bold", bg="#00226d", fg = "#fff",relief = FLAT, activebackground="#6585cd")
        self.btnConfirma.place(width=270,height=50,relx = 0.14, rely= 0.80)
        self.tela.mainloop()



#telaself.tela()
#telaConectar()
#telaEsqSenha()
#telaself.tela()
#telaself.tela()
#root.mainloop()
if __name__ == "__main__":
    CadastroLogin('', '', '')