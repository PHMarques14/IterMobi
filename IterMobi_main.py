import os
from SGBD_IterMobi import *
from tkinter import *
from threading import Timer
import speech_recognition as sr
from gtts import gTTS
from pygame import mixer, time
from validate_email import validate_email
from random import randint

useBanco()

class Usuario:
    def __init__(self, nome, email, __senha):
        self.nome = nome
        self.email = email
        self.__senha = __senha

        self.cadastrar()
    
    def cadastrar(self):
        c = ''
        for p in self.__senha:
            e = ord(p)

            if e % 2 == 0:
                d = f'{chr(e)}{chr(e-1)}'
                e = e//2
            else:
                if e == 33:
                    d = f'{chr(e)}{chr(e+1)}'
                    e *= 2
                else:
                    d = f'{chr(e)}{chr(e+1)}'
                    e *= 2

            c = (c+f'{e}{d}')
        print(c)

        try:
            registrar(self.nome, self.email, c)
        except:
            return 1

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
        self.img3 = PhotoImage(file="mic.png")
        self.img4 = PhotoImage(file="seta.png")
        self.img5 = PhotoImage(file="olho.png")

        self.lblLogo = Label(self.tela, image=self.img2, bg="#cfcbcb")        
        self.lblLogo.place(relx=0.25, rely=0.4)
        t = Timer(2, lambda: self.cadastro(0))
        t.start()
        self.tela.mainloop()
 
    def cadastro(self, event):
        '''Tela de cadastro do aplicativo'''
        self.lblLogo.destroy()
        try:
            self.lblAviso.destroy()
        except:
            pass
        try:
            self.btnEsqSenha.destroy()
            self.btnConfirma.destroy()
            self.btnCadastroLogin.destroy()
            self.mainLbl.destroy()
            self.lblEmail.destroy()
            self.lblSenha.destroy()
            self.entryEmail.destroy()
            self.entrySenha.destroy()
            self.btnVer1.destroy()
            self.btnVer2.destroy()
        except:
            pass
        
        self.lblTri = Label(self.tela, image=self.img1, bg="#cfcbcb")        
        self.lblTri.place(relx=0, rely=0)

        self.mainLbl = Label(self.tela, text="CRIE SUA CONTA", font="Helvetica 23 bold", bg = "#cfcbcb", fg = "#00226d")
        self.mainLbl.place(relx = 0.14,rely=0.1)
        self.lblNome = Label(self.tela, text="NOME", font="Arial 9", bg="#cfcbcb", fg = "#00226d")
        self.lblNome.place(relx = 0.14, rely= 0.18)
        self.lblEmail = Label(self.tela, text="EMAIL", font="Arial 9", bg="#cfcbcb", fg = "#00226d")
        self.lblEmail.place(relx = 0.14, rely= 0.32)
        self.lblSenha = Label(self.tela, text="SENHA", font="Arial 9", bg="#cfcbcb", fg = "#00226d")
        self.lblSenha.place(relx = 0.14, rely= 0.45)
        self.lblConfSenha = Label(self.tela, text="CONFIRMAR SENHA", font="Arial 9", bg="#cfcbcb", fg = "#00226d")
        self.lblConfSenha.place(relx = 0.14, rely= 0.58)

        self.entryNome = Entry(self.tela, relief = FLAT, font= "Helvetica 14")
        self.entryNome.place(width=270,height=50,relx = 0.14, rely= 0.23)
        self.entryNome.focus_set()
        self.entryEmail = Entry(self.tela, relief = FLAT, font= "Helvetica 14")
        self.entryEmail.place(width=270,height=50,relx = 0.14, rely= 0.36)
        self.entrySenha = Entry(self.tela, relief = FLAT, font= "Helvetica 14")
        self.entrySenha.place(width=270,height=50,relx = 0.14, rely= 0.49)
        self.entrySenha.config(show='*')
        self.entryConfSenha = Entry(self.tela, relief = FLAT, font= "Helvetica 14")
        self.entryConfSenha.place(width=270,height=50,relx = 0.14, rely= 0.62)
        self.entryConfSenha.config(show='*')
        self.btnVer1 = Label(self.tela, image=self.img5, bg='white')
        self.btnVer1.bind('<Button-1>', lambda event, arg='ver1': self.acao(event, arg))
        self.btnVer1.bind('<ButtonRelease-1>', lambda event, arg='esc1': self.acao(event, arg))
        self.btnVer1.place(relx= 0.745, rely=0.49)
        self.btnVer2 = Label(self.tela, image=self.img5, bg='white')
        self.btnVer2.bind('<Button-1>', lambda event, arg='ver2': self.acao(event, arg))
        self.btnVer2.bind('<ButtonRelease-1>', lambda event, arg='esc2': self.acao(event, arg))
        self.btnVer2.place(relx=0.745, rely=0.62)
        self.btnConfirma = Button(self.tela, text="CADASTRAR", font="Arial 11 bold", bg="#00226d", fg = "#fff",relief = FLAT, activebackground="#6585cd", command=lambda: self.home(0))
        self.btnConfirma.place(width=270,height=50,relx = 0.14, rely= 0.80)
        self.btnCadastroLogin = Label(self.tela, text="JÁ TEM CADASTRO? CLIQUE AQUI", font="Arial 9 underline", bg="#cfcbcb", fg = "#000", relief = FLAT)
        self.btnCadastroLogin.place(relx = 0.23, rely= 0.90)
        self.btnCadastroLogin.bind('<Button-1>', self.login)

    def login(self, event):
        '''Tela de login do aplicativo'''
        try:
            self.lblAviso.destroy()
        except:
            pass
        self.lblNome.destroy()
        self.entryNome.destroy()
        self.lblConfSenha.destroy()
        self.entryConfSenha.destroy()
        self.btnVer2.destroy()

        self.mainLbl.config(text="CONECTAR", font="Helvetica 23 bold", bg = "#cfcbcb", fg = "#00226d")
        self.mainLbl.place(relx = 0.25,rely=0.1)
        self.lblEmail.config(text="EMAIL", font="Arial 9", bg="#cfcbcb", fg = "black")
        self.lblEmail.place(relx = 0.14, rely= 0.32)
        self.lblSenha.config(text="SENHA", font="Arial 9", bg="#cfcbcb", fg = "black")
        self.lblSenha.place(relx = 0.14, rely= 0.47)
        self.btnEsqSenha = Label(self.tela, text="ESQUECI A SENHA", font="Arial 9 underline", bg="#cfcbcb", fg = "black", relief = FLAT)
        self.btnEsqSenha.place(relx = 0.14, rely= 0.58)
        self.btnEsqSenha.bind('<Button-1>', self.esqueceuSenha)
        self.btnCadastroLogin.config(text="CADASTRE-SE PARA CONTINUAR", font="Arial 9 underline", bg="#cfcbcb", fg = "black")
        self.btnCadastroLogin.place(relx = 0.14, rely= 0.8)
        self.btnCadastroLogin.bind('<Button-1>', self.cadastro)

        self.entryEmail.config(relief = FLAT, font= "Helvetica 14")
        self.entryEmail.place(width=270,height=50,relx = 0.14, rely= 0.36)
        self.entryEmail.focus_set()
        self.entrySenha.config(relief = FLAT, font= "Helvetica 14")
        self.entrySenha.config(show='*')
        self.entrySenha.place(width=270,height=50,relx = 0.14, rely= 0.5)
        self.entrySenha.bind('<Return>', lambda event: self.home(1))

        self.btnVer1.place(relx=0.745, rely=0.5)

        self.btnConfirma.config(text="ENTRAR", font="Arial 11 bold", bg="#00226d", fg = "#fff",relief = FLAT, activebackground="#6585cd", command=lambda: self.home(1))
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
        self.mainLbl.config(text=self.texto, font="Helvetica 23 bold", bg = "#cfcbcb", fg = "#00226d")
        self.mainLbl.place(relx = 0.23,rely=0.1)
        self.infoLbl= Label(self.tela, text = self.texto2, font="Helvetica 11", justify=LEFT, bg = "#cfcbcb", fg = "#000")
        self.infoLbl.place(relx = 0.07,rely=0.3)
        self.lblEmail.config(text="DIGITE SEU EMAIL", font="Arial 11", bg="#cfcbcb", fg = "black")
        self.lblEmail.place(relx = 0.13, rely= 0.5)
        self.entryEmail.config(relief = FLAT, font= "Helvetica 14")
        self.entryEmail.place(width=270,height=50,relx = 0.13, rely= 0.56)
        self.entryEmail.focus_set()
        self.entryEmail.delete(0, END)
        self.entryEmail.unbind('<Key>', None)
        self.entryEmail.bind('<Return>', self.enviarcodigo)
        self.btnConfirma.config(text="ENVIAR", font="Arial 11 bold", bg="#00226d", fg = "#fff",relief = FLAT, activebackground="#6585cd", command=lambda: self.enviarcodigo(0))
        self.btnConfirma.place(width=270,height=50,relx = 0.14, rely= 0.80)
        self.btnConfirma.bind('<Return>', self.enviarcodigo)

    def codigo(self, event):
        '''Enivia um código ao e-mail inserido pelo usuário'''
        self.lblEmail.destroy()
        self.entryEmail.destroy()

        self.texto = """ESQUECEU A
        SENHA?"""
        self.texto2 = """CASO O CÓDIGO NÃO TENHA SIDO 
        ENVIADO, CLIQUE NO BOTÃO
        ABAIXO PARA REENVIÁ-LO"""
        self.mainLbl.config(text=self.texto, font="Helvetica 23 bold", bg = "#cfcbcb", fg = "#00226d")
        self.mainLbl.place(relx = 0.23,rely=0.1)
        self.infoLbl.config(text = self.texto2, font="Helvetica 11",justify=LEFT, bg = "#cfcbcb", fg = "#000")
        self.infoLbl.place(relx = 0.1,rely=0.5)
        self.lblCodigo = Label(self.tela, text="DIGITE O CÓDIGO DE CONFIRMAÇÃO", font="Arial 11", bg="#cfcbcb", fg = "black")
        self.lblCodigo.place(relx = 0.13, rely= 0.3)
        self.entryCodigo = Entry(self.tela, relief = FLAT, font= "Helvetica 16", justify=CENTER)
        self.entryCodigo.place(width=270,height=50,relx = 0.13, rely= 0.36)
        self.entryCodigo.focus_set()
        self.entryCodigo.bind('<Return>', self.alterar)
        self.btnConfirma.config(command=lambda: self.alterar(0))

        self.btnReenvia = Button(self.tela, text="REENVIAR CÓDIGO", font="Arial 11 bold", bg="#6585cd", fg = "#fff",relief = FLAT, activebackground="#6585cd", command=self.enviarcodigo)
        self.btnReenvia.place(width=230,height=40,relx = 0.2, rely= 0.64)

    def alterar(self, event):
        self.c = self.entryCodigo.get()
        if self.c != self.cod:
            self.entryCodigo.config(text='Código incorreto!')
            None
        else:
            '''Altera a senha antiga da conta do usuário e insere uma nova senha ao banco de dados'''
            self.infoLbl.destroy()
            self.lblCodigo.destroy()
            self.entryCodigo.destroy()
            self.btnReenvia.destroy()

            self.texto = """ESQUECEU A
            SENHA?"""

            self.mainLbl.config(text=self.texto, font="Helvetica 23 bold", bg = "#cfcbcb", fg = "#00226d")
            self.mainLbl.place(relx = 0.24,rely=0.1)
            self.lblSenha = Label(self.tela, text="SENHA", font="Arial 11", bg="#cfcbcb", fg = "black")
            self.lblSenha.place(relx = 0.14, rely= 0.32)
            self.lblRepeteSenha = Label(self.tela, text="REPITA SUA NOVA SENHA", font="Arial 11", bg="#cfcbcb", fg = "black")
            self.lblRepeteSenha.place(relx = 0.14, rely= 0.47)

            self.entrySenha = Entry(self.tela, relief = FLAT, font= "Helvetica 11")
            self.entrySenha.config(show='*')
            self.entrySenha.place(width=270,height=50,relx = 0.14, rely= 0.36)
            self.entryRepeteSenha = Entry(self.tela, relief = FLAT, font= "Helvetica 11")
            self.entryRepeteSenha.config(show='*')
            self.entryRepeteSenha.place(width=270,height=50,relx = 0.14, rely= 0.5)
            self.entryRepeteSenha.bind('<Return>', self.home)
            
            self.btnConfirma.config(text="CONFIRMAR", font="Arial 11 bold", bg="#00226d", fg = "#fff",relief = FLAT, activebackground="#6585cd", command=lambda: self.home(2))
            self.btnConfirma.place(width=270,height=50,relx = 0.14, rely= 0.80)
            self.btnConfirma.bind('<Return>', self.home)
    
    def enviarcodigo(self, event):
        try:
            email = self.entryEmail.get()
            self.cod = randint(100000, 999999)
            senha = open('senha.txt', 'r')
            self.cod = str(self.cod)

            to = str(email)
            user = 'itermobi83@gmail.com'
            smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
            smtpserver.ehlo()
            smtpserver.starttls()
            smtpserver.ehlo
            smtpserver.login(user, senha.read())
            header = 'To:' + to + '\n' + 'From: ' + user + '\n' + 'Subject:Código de alteração de senha \n'
            msg = header+'\nOlá querido usuário!\nAqui está o código para trocar sua senha: '+self.cod+'. Para trocá-la, basta estar no aplicativo e digitar esse código no espaço determinado.\nAtenciosamente,\nEquipe IterMobi\n\n'
            smtpserver.sendmail(user, to, msg.encode())
            print('done!')
            smtpserver.close()
            
            return self.codigo(0)
        except:
            self.entryEmail.config(fg='red')
            self.entryEmail.delete(0, END)
            self.entryEmail.insert(0, 'Digite um email!')
            self.entryEmail.bind('<Button-1>', lambda event, arg=1: self.acao(event, arg))
            self.entryEmail.bind('<Key>', lambda event, arg=1: self.acao(event, arg))        

    def home(self, event):
        if event == 0:
            self.nome = self.entryNome.get()
            self.email = self.entryEmail.get()
            self.__senha = self.entrySenha.get()
            self.confSenha = self.entryConfSenha.get()

            if self.nome == '' or self.email == '' or self.__senha == '' or self.confSenha == '':
                if self.nome == '' and self.email == '' and self.__senha == '' and self.confSenha == '':
                    self.entryNome.config(fg='red')
                    self.entryEmail.config(fg='red')
                    self.entrySenha.config(fg='red', show='')
                    self.entryConfSenha.config(fg='red', show='')

                    self.entryNome.insert(0, 'Digite seu nome!')
                    self.entryEmail.insert(0, 'Digite um email!')
                    self.entrySenha.insert(0, 'Digite uma senha!')
                    self.entryConfSenha.insert(0, 'Repita a senha!')

                    self.entryNome.bind('<Button-1>', lambda event, arg=0: self.acao(event, arg))
                    self.entryEmail.bind('<Button-1>', lambda event, arg=1: self.acao(event, arg))
                    self.entrySenha.bind('<Button-1>', lambda event, arg=2: self.acao(event, arg))
                    self.entryConfSenha.bind('<Button-1>', lambda event, arg=3: self.acao(event, arg))

                    self.entryNome.bind('<Key>', lambda event, arg=0: self.acao(event, arg))
                    self.entryEmail.bind('<Key>', lambda event, arg=1: self.acao(event, arg))
                    self.entrySenha.bind('<Key>', lambda event, arg=2: self.acao(event, arg))
                    self.entryConfSenha.bind('<Key>', lambda event, arg=3: self.acao(event, arg))
                    None
                elif self.nome == '' and self.email == '' and self.__senha == '':
                    self.entryNome.config(fg='red')
                    self.entryEmail.config(fg='red')
                    self.entrySenha.config(fg='red', show='')

                    self.entryNome.insert(0, 'Digite seu nome!')
                    self.entryEmail.insert(0, 'Digite um email!')
                    self.entrySenha.insert(0, 'Digite uma senha!')

                    self.entryNome.bind('<Button-1>', lambda event, arg=0: self.acao(event, arg))
                    self.entryEmail.bind('<Button-1>', lambda event, arg=1: self.acao(event, arg))
                    self.entrySenha.bind('<Button-1>', lambda event, arg=2: self.acao(event, arg))

                    self.entryNome.bind('<Key>', lambda event, arg=0: self.acao(event, arg))
                    self.entryEmail.bind('<Key>', lambda event, arg=1: self.acao(event, arg))
                    self.entrySenha.bind('<Key>', lambda event, arg=2: self.acao(event, arg))
                    None
                elif self.nome == '' and self.email == '' and self.confSenha == '':
                    self.entryNome.config(fg='red')
                    self.entryEmail.config(fg='red')
                    self.entryConfSenha.config(fg='red', show='')

                    self.entryNome.insert(0, 'Digite seu nome!')
                    self.entryEmail.insert(0, 'Digite um email!')
                    self.entryConfSenha.insert(0, 'Repita a senha!')

                    self.entryNome.bind('<Button-1>', lambda event, arg=0: self.acao(event, arg))
                    self.entryEmail.bind('<Button-1>', lambda event, arg=1: self.acao(event, arg))
                    self.entryConfSenha.bind('<Button-1>', lambda event, arg=3: self.acao(event, arg))

                    self.entryNome.bind('<Key>', lambda event, arg=0: self.acao(event, arg))
                    self.entryEmail.bind('<Key>', lambda event, arg=1: self.acao(event, arg))
                    self.entryConfSenha.bind('<Key>', lambda event, arg=3: self.acao(event, arg))
                    None
                elif self.nome == '' and self.__senha == '' and self.confSenha == '':
                    self.entryNome.config(fg='red')
                    self.entrySenha.config(fg='red', show='')
                    self.entryConfSenha.config(fg='red', show='')

                    self.entryNome.insert(0, 'Digite seu nome!')
                    self.entrySenha.insert(0, 'Digite uma senha!')
                    self.entryConfSenha.insert(0, 'Repita a senha!')

                    self.entryNome.bind('<Button-1>', lambda event, arg=0: self.acao(event, arg))
                    self.entrySenha.bind('<Button-1>', lambda event, arg=2: self.acao(event, arg))
                    self.entryConfSenha.bind('<Button-1>', lambda event, arg=3: self.acao(event, arg))

                    self.entryNome.bind('<Key>', lambda event, arg=0: self.acao(event, arg))
                    self.entrySenha.bind('<Key>', lambda event, arg=2: self.acao(event, arg))
                    self.entryConfSenha.bind('<Key>', lambda event, arg=3: self.acao(event, arg))
                    None
                elif self.email == '' and self.__senha == '' and self.confSenha == '':
                    self.entryEmail.config(fg='red')
                    self.entrySenha.config(fg='red', show='')
                    self.entryConfSenha.config(fg='red', show='')

                    self.entryEmail.insert(0, 'Digite um email!')
                    self.entrySenha.insert(0, 'Digite uma senha!')
                    self.entryConfSenha.insert(0, 'Repita a senha!')

                    self.entryEmail.bind('<Button-1>', lambda event, arg=1: self.acao(event, arg))
                    self.entrySenha.bind('<Button-1>', lambda event, arg=2: self.acao(event, arg))
                    self.entryConfSenha.bind('<Button-1>', lambda event, arg=3: self.acao(event, arg))

                    self.entryEmail.bind('<Key>', lambda event, arg=1: self.acao(event, arg))
                    self.entrySenha.bind('<Key>', lambda event, arg=2: self.acao(event, arg))
                    self.entryConfSenha.bind('<Key>', lambda event, arg=3: self.acao(event, arg))
                    None
                elif self.nome == '' and self.email == '':
                    self.entryNome.config(fg='red')
                    self.entryEmail.config(fg='red')

                    self.entryNome.insert(0, 'Digite seu nome!')
                    self.entryEmail.insert(0, 'Digite um email!')

                    self.entryNome.bind('<Button-1>', lambda event, arg=0: self.acao(event, arg))
                    self.entryEmail.bind('<Button-1>', lambda event, arg=1: self.acao(event, arg))

                    self.entryNome.bind('<Key>', lambda event, arg=0: self.acao(event, arg))
                    self.entryEmail.bind('<Key>', lambda event, arg=1: self.acao(event, arg))
                    None
                elif self.nome == '' and self.__senha == '':
                    self.entryNome.config(fg='red')
                    self.entrySenha.config(fg='red', show='')

                    self.entryNome.insert(0, 'Digite seu nome!')
                    self.entrySenha.insert(0, 'Digite uma senha!')

                    self.entryNome.bind('<Button-1>', lambda event, arg=0: self.acao(event, arg))
                    self.entrySenha.bind('<Button-1>', lambda event, arg=2: self.acao(event, arg))

                    self.entryNome.bind('<Key>', lambda event, arg=0: self.acao(event, arg))
                    self.entrySenha.bind('<Key>', lambda event, arg=2: self.acao(event, arg))
                    None
                elif self.nome == '' and self.confSenha == '':
                    self.entryNome.config(fg='red')
                    self.entryConfSenha.config(fg='red', show='')

                    self.entryNome.insert(0, 'Digite seu nome!')
                    self.entryConfSenha.insert(0, 'Repita a senha!')

                    self.entryNome.bind('<Button-1>', lambda event, arg=0: self.acao(event, arg))
                    self.entryConfSenha.bind('<Button-1>', lambda event, arg=3: self.acao(event, arg))

                    self.entryNome.bind('<Key>', lambda event, arg=0: self.acao(event, arg))
                    self.entryConfSenha.bind('<Key>', lambda event, arg=3: self.acao(event, arg))
                    None
                elif self.email == '' and self.__senha == '':
                    self.entryEmail.config(fg='red')
                    self.entrySenha.config(fg='red', show='')

                    self.entryEmail.insert(0, 'Digite um email!')
                    self.entrySenha.insert(0, 'Digite uma senha!')

                    self.entryEmail.bind('<Button-1>', lambda event, arg=1: self.acao(event, arg))
                    self.entrySenha.bind('<Button-1>', lambda event, arg=2: self.acao(event, arg))

                    self.entryEmail.bind('<Key>', lambda event, arg=1: self.acao(event, arg))
                    self.entrySenha.bind('<Key>', lambda event, arg=2: self.acao(event, arg))
                    None
                elif self.email == '' and self.confSenha == '':
                    self.entryNome.config(fg='red')
                    self.entryConfSenha.config(fg='red', show='')

                    self.entryNome.insert(0, 'Digite seu nome!')
                    self.entryConfSenha.insert(0, 'Repita a senha!')

                    self.entryNome.bind('<Button-1>', lambda event, arg=0: self.acao(event, arg))
                    self.entryConfSenha.bind('<Button-1>', lambda event, arg=3: self.acao(event, arg))

                    self.entryNome.bind('<Key>', lambda event, arg=0: self.acao(event, arg))
                    self.entryConfSenha.bind('<Key>', lambda event, arg=3: self.acao(event, arg))
                    None
                elif self.__senha == '' and self.confSenha == '':
                    self.entrySenha.config(fg='red', show='')
                    self.entryConfSenha.config(fg='red', show='')

                    self.entrySenha.insert(0, 'Digite uma senha!')
                    self.entryConfSenha.insert(0, 'Repita a senha!')

                    self.entrySenha.bind('<Button-1>', lambda event, arg=2: self.acao(event, arg))
                    self.entryConfSenha.bind('<Button-1>', lambda event, arg=3: self.acao(event, arg))

                    self.entrySenha.bind('<Key>', lambda event, arg=2: self.acao(event, arg))
                    self.entryConfSenha.bind('<Key>', lambda event, arg=3: self.acao(event, arg))
                    None
                elif self.nome == '':
                    self.entryNome.config(fg='red')
                    self.entryNome.insert(0, 'Digite seu nome!')
                    self.entryNome.bind('<Button-1>', lambda event, arg=0: self.acao(event, arg))
                    self.entryNome.bind('<Key>', lambda event, arg=0: self.acao(event, arg))
                    None
                elif self.email == '':
                    self.entryEmail.config(fg='red')
                    self.entryEmail.insert(0, 'Digite um email!')
                    self.entryEmail.bind('<Button-1>', lambda event, arg=1: self.acao(event, arg))
                    self.entryEmail.bind('<Key>', lambda event, arg=1: self.acao(event, arg))
                    None
                elif self.__senha == '':
                    self.entrySenha.config(fg='red', show='')
                    self.entrySenha.insert(0, 'Digite uma senha!')
                    self.entrySenha.bind('<Button-1>', lambda event, arg=2: self.acao(event, arg))
                    self.entrySenha.bind('<Key>', lambda event, arg=2: self.acao(event, arg))
                    None
                elif self.confSenha == '':
                    self.entryConfSenha.config(fg='red', show='')
                    self.entryConfSenha.insert(0, 'Repita a senha!')
                    self.entryConfSenha.bind('<Button-1>', lambda event, arg=3: self.acao(event, arg))
                    self.entryConfSenha.bind('<Key>', lambda event, arg=3: self.acao(event, arg))
                    None
            elif self.nome == 'Digite seu nome!' or self.email == 'Digite um email!' or self.__senha == 'Digite uma senha!' or self.confSenha == 'Repita a senha!':
                None
            else:
                pass
        elif event == 1:
            self.email = self.entryEmail.get()
            self.__senha = self.entrySenha.get()
            if self.email == '' or self.__senha == '':
                if self.email == '' and self.__senha == '':
                    self.entryEmail.config(fg='red')
                    self.entrySenha.config(fg='red', show='')

                    self.entryEmail.insert(0, 'Digite um email!')
                    self.entrySenha.insert(0, 'Digite uma senha!')

                    self.entryEmail.bind('<Button-1>', lambda event, arg=1: self.acao(event, arg))
                    self.entrySenha.bind('<Button-1>', lambda event, arg=2: self.acao(event, arg))

                    self.entryEmail.bind('<Key>', lambda event, arg=1: self.acao(event, arg))
                    self.entrySenha.bind('<Key>', lambda event, arg=2: self.acao(event, arg))
                    None
                elif self.email == '':
                    self.entryEmail.config(fg='red')
                    self.entryEmail.insert(0, 'Digite um email!')
                    self.entryEmail.bind('<Button-1>', lambda event, arg=1: self.acao(event, arg))
                    self.entryEmail.bind('<Key>', lambda event, arg=1: self.acao(event, arg))
                    None
                elif self.__senha == '':
                    self.entrySenha.config(fg='red', show='')
                    self.entrySenha.insert(0, 'Digite uma senha!')
                    self.entrySenha.bind('<Button-1>', lambda event, arg=2: self.acao(event, arg))
                    self.entrySenha.bind('<Key>', lambda event, arg=2: self.acao(event, arg))
                    None
            elif self.email == 'Digite um email!' or self.__senha == 'Digite uma senha!':
                None
            else:
                pass
        elif event == 2:
            self.__senha = self.entrySenha.get()
            self.confSenha = self.entryRepeteSenha.get()
            if self.__senha == '' or self.confSenha == '':
                if self.__senha == '' and self.confSenha == '':
                    self.entrySenha.config(fg='red', show='')
                    self.entryConfSenha.config(fg='red', show='')

                    self.entrySenha.insert(0, 'Digite uma senha!')
                    self.entryConfSenha.insert(0, 'Repita a senha!')

                    self.entrySenha.bind('<Button-1>', lambda event, arg=2: self.acao(event, arg))
                    self.entryConfSenha.bind('<Button-1>', lambda event, arg=3: self.acao(event, arg))

                    self.entrySenha.bind('<Key>', lambda event, arg=2: self.acao(event, arg))
                    self.entryConfSenha.bind('<Key>', lambda event, arg=3: self.acao(event, arg))
                    None
                elif self.__senha == '':
                    self.entrySenha.config(fg='red', show='')
                    self.entrySenha.insert(0, 'Digite uma senha!')
                    self.entrySenha.bind('<Button-1>', lambda event, arg=2: self.acao(event, arg))
                    self.entrySenha.bind('<Key>', lambda event, arg=2: self.acao(event, arg))
                    None
                elif self.confSenha == '':
                    self.entryConfSenha.config(fg='red', show='')
                    self.entryConfSenha.insert(0, 'Repita a senha!')
                    self.entryConfSenha.bind('<Button-1>', lambda event, arg=3: self.acao(event, arg))
                    self.entryConfSenha.bind('<Key>', lambda event, arg=3: self.acao(event, arg))
                    None
            elif self.__senha == 'Digite uma senha!' or self.confSenha == 'Repita a senha!':
                None
            else:
                verificar = 1
                pass

        if event == 0:
            self.emailUsuario = self.entryEmail.get()
            verificar = self.verificar(self.emailUsuario)
            print('ok')
            if verificar != 1:
                print(verificar)
                self.entryEmail.config(fg='red')
                self.entryEmail.delete(0, END)
                self.entryEmail.insert(0, 'Digite um email!')
                self.entryEmail.bind('<Button-1>', lambda event, arg=1: self.acao(event, arg))
                self.entryEmail.bind('<Key>', lambda event, arg=1: self.acao(event, arg))
                pass
            else:
                print('verificado')
                cad = verificarConta(self.emailUsuario)
                print(cad)
                if cad == '':
                    if self.__senha < 8:
                        self.entrySenha.config(fg='red', show='', font='Helvetica 11')
                        self.entrySenha.delete(0, END)
                        self.entrySenha.insert(0, 'A senha deve conter pelo menos 8 caracteres!')
                        self.entrySenha.bind('<Button-1>', lambda event, arg=2: self.acao(event, arg))
                        self.entrySenha.bind('<Key>', lambda event, arg=2: self.acao(event, arg))
                        pass
                    else:
                        if self.confSenha != self.__senha or self.__senha != self.confSenha:
                            self.entryConfSenha.config(fg='red', show='', font='Helvetica 12')
                            self.entryConfSenha.delete(0, END)
                            self.entryConfSenha.insert(0, 'Confirmação incorreta!')
                            self.entryConfSenha.bind('<Button-1>', lambda event, arg=2: self.acao(event, arg))
                            self.entryConfSenha.bind('<Key>', lambda event, arg=2: self.acao(event, arg))
                            pass
                        else:
                            Usuario(self.nome, self.email, self.__senha)
                else:
                    print('ok2')
                    self.lblAviso = Label(self.tela, text='''Essa conta já está cadastrada.
ENTRE PARA CONTINUAR.''', font='Arial 14 bold', bg='#6585cd', bd=2, relief=GROOVE)
                    self.lblAviso.place(relx=0.12, rely=0.71)
                    t = Timer(4, lambda: self.acao(0, 'aviso'))
                    t.start()
                    verificar = 0
                    None
        elif event == 1:
            verificar = self.verificar(self.email)
            if verificar != 1:
                self.entryEmail.config(fg='red')
                self.entryEmail.delete(0, END)
                self.entryEmail.insert(0, 'Digite um email!')
                self.entryEmail.bind('<Button-1>', lambda event, arg=1: self.acao(event, arg))
                self.entryEmail.bind('<Key>', lambda event, arg=1: self.acao(event, arg))    
                pass
            else:
                vc = verificarConta(self.email)
                if vc == '':
                    print('pq')
                    self.lblAviso = Label(self.tela, text='''Essa conta não existe.
CADASTRE-SE PARA CONTINUAR.''', font='Arial 14 bold', bg='#6585cd', bd=2, relief=GROOVE)
                    self.lblAviso.place(relx=0.146, rely=0.62)
                    t = Timer(4, lambda: self.acao(0, 'aviso'))
                    t.start()
                    verificar = 0
                    None
                else:
                    vs = verificarSenha(self.email, self.__senha)
                    if vs == 1:
                        self.entrySenha.config(fg='red', show='')
                        self.entrySenha.delete(0, END)
                        self.entrySenha.insert(0, 'Senha incorreta!')
                        self.entrySenha.bind('<Button-1>', lambda event, arg=2: self.acao(event, arg))
                        self.entrySenha.bind('<Key>', lambda event, arg=2: self.acao(event, arg))
                        print('é igual a 1')
                        verificar = 0
                        None
                    elif vs == 0:
                        print('ok')
                        pass
        
        try:
            self.lblSeta.destroy()
            self.lblEsc.destroy()
        except:
            pass
        if verificar == 0:
            None
        else:
            if event == 0:
                self.lblTri.destroy()
                self.lblNome.destroy()
                self.entryNome.destroy()
                self.lblConfSenha.destroy()
                self.entryConfSenha.destroy()
                self.btnConfirma.destroy()
                self.btnCadastroLogin.destroy()
                self.lblEmail.destroy()
                self.lblSenha.destroy()
                self.entryEmail.destroy()
                self.entrySenha.destroy()
                self.btnVer1.destroy()
                self.btnVer2.destroy()
                pass
            elif event == 1:
                self.lblTri.destroy()
                self.lblNome.destroy()
                self.lblEmail.destroy()
                self.lblSenha.destroy()
                self.entryEmail.destroy()
                self.entrySenha.destroy()
                self.btnEsqSenha.destroy()
                self.btnVer1.destroy()
                pass
            elif event == 2:
                self.lblSenha.destroy()
                self.entrySenha.destroy()
                self.lblRepeteSenha.destroy()
                self.entryRepeteSenha.destroy()
                self.btnConfirma.destroy()    
                pass
            else:
                self.lblBusca.destroy()   
                self.entryBusca.destroy()
                self.lblMic.destroy()
                self.lblLugRec.destroy()
                pass
            try:
                self.lblTri.destroy()
                self.mainLbl.destroy()
                self.lblNome.destroy()
                self.entryNome.destroy()
                self.lblConfSenha.destroy()
                self.entryConfSenha.destroy()
                self.btnConfirma.destroy()
                self.btnCadastroLogin.destroy()
                self.lblEmail.destroy()
                self.lblSenha.destroy()
                self.entryEmail.destroy()
                self.entrySenha.destroy()
            except:
                pass
            
            self.mainLbl = Label(text="IterMobi", font="Beirut 28", bg = "#cfcbcb", fg = "#30343F", justify=LEFT)
            self.mainLbl.place(relx = 0.02,rely=0.03)

            self.lblBusca = Label(self.tela, bg = "#00226d")
            self.lblBusca.place(width=400,height=66,relx = 0, rely= 0.12)
            self.entryBusca = Entry(self.lblBusca, relief = FLAT, font= "Helvetica 14")
            self.entryBusca.place(width=309,height=54,relx = 0.01, rely= 0.05)
            self.entryBusca.bind('<Return>', self.escolha)

            self.lblMic = Label(self.tela, image=self.img3)
            self.lblMic.place(x=315,y=86)
            self.lblMic.bind('<Button-1>', self.microfone)

            self.lblLugRec = Label(self.tela, text="Linhas recentes:", font="Beirut 18", bg = "#cfcbcb", fg = "#5E5E5E")
            self.lblLugRec.place(relx = 0.02, rely=0.34)
            self.lblSeta = Button(self.tela)
    
    def escolha(self, event):
        self.n = self.entryBusca.get()
        self.lbl = procurar(self.n)
        print(self.lbl)
        if self.lbl == 1:
            None
        else:
            self.lblLugRec.destroy()
            try:
                self.btnAlertaMoto.destroy()
                self.lblPLugar.destroy()
                self.lblPLugarEnder.destroy()
                self.lblLinha.destroy()
                self.lblnumLinha.destroy()
                self.lblSeta.destroy()
            except:
                pass
            
            self.mainLbl.config(text="Escolha o ônibus", font="Beirut 24 bold", bg = "#6585cd", fg = "white")
            self.mainLbl.place(width=380,height=82,relx = 0,rely=0)

            self.lblSeta = Button(self.tela, image= self.img4, bg = "#6585cd", relief=FLAT, activebackground="#6585cd", command=lambda:self.home(3))
            self.lblSeta.place(width=50,height=50 ,x=5,y=20)
            self.lblEsc = Label(self.tela)
            self.criarEscolhas()

    def criarEscolhas(self):
        self.lblEsc.place(width=400,height=400,x= -2, y = 145)
        for i in self.lbl:
            l = locTrajeto(i)
            l = str(l)
            self.lblOnibus = Button(self.lblEsc, width=400, text=i, font="Beirut 18", bg = "#2955b6", fg = "black", relief=FLAT, command=lambda: self.notificar(l))
            self.lblOnibus.pack()
    def notificar(self, event):
        self.entryBusca.config(text=self.n)
        self.lblSeta.config(command=lambda:self.escolha(0))
        self.btnAlertaMoto = Button( self.tela, text="Alertar motorista!", font="Beirut 18", bg = "red", fg = "black", relief=FLAT, command=self.enviar)
        self.btnAlertaMoto.place(width=400,height=60,x= -2, y = 455)

        self.lblPLugar = Label(self.tela, text=f"Linha: {event}", font="Beirut 18", bg = "#ededed", fg = "black", anchor= "nw")
        self.lblPLugar.place(width=400,height=80,x= -2, y = 517)
        self.lblPLugarEnder = Label(self.tela, text="Local: Graal Resende", font="Beirut 12", bg = "#ededed", fg = "#30343F", anchor= "w")
        self.lblPLugarEnder.place(x= -2, y = 557)

        self.lblLinha = Label(self.tela, text="Ônibus selecionado:", font="Beirut 18", bg = "#ededed", fg = "black", anchor= "nw")
        self.lblLinha.place(width=400,height=80,x= -2, y = 600)
        self.lblnumLinha = Label(self.tela, text="372", font="Beirut 40", bg = "#ededed", fg = "#30343F")
        self.lblnumLinha.place(x= 260, y = 600)
    def enviar(self):
        noti = open('noti.txt', 'w+')
        noti.write(self.email)
        noti.write('\n-22.458704, -44.441193')
        
    def acao(self, event, arg):
        if arg == 0:
            self.entryNome.config(fg='black')
            self.entryNome.delete(0, END)
            self.entryNome.unbind('<Key>')
            self.entryNome.unbind('Button-1')
        elif arg == 1:
            self.entryEmail.config(fg='black')
            self.entryEmail.delete(0, END)
            self.entryEmail.unbind('<Key>')
            self.entryEmail.unbind('<Button-1>')
        elif arg == 2:
            self.entrySenha.config(fg='black', show='*', font='Helvetica 14')
            self.entrySenha.delete(0, END)
            self.entrySenha.unbind('<Key>')
            self.entrySenha.unbind('<Button-1>')
        elif arg == 3:
            self.entryConfSenha.config(fg='black', show='*')
            self.entryConfSenha.delete(0, END)
            self.entryConfSenha.unbind('<Key>')
            self.entryConfSenha.unbind('<Button-1>')
        elif arg == 'aviso':
            self.lblAviso.destroy()
        elif arg == 'ver1':
            self.btnVer1.config(bg='#cfcbcb')
            self.entrySenha.config(show='')
            self.entrySenha.unbind('<ButtonRelease-1>')
        elif arg == 'ver2':
            self.btnVer2.config(bg='#cfcbcb')
            self.entryConfSenha.config(show='')
            self.entryConfSenha.unbind('<ButtonRelease-1>')
        elif arg == 'esc1':
            self.btnVer1.config(bg='white')
            self.entrySenha.config(show='*')
            self.entrySenha.unbind('<Button-1>')
        else:
            self.btnVer2.config(bg='white')
            self.entryConfSenha.config(show='*')
            self.entryConfSenha.unbind('<Button-1>')


    def microfone(self, event):
        #Função para ouvir e reconhecer a fala
        #Habilita o microfone do usuário
        microfone = sr.Recognizer()
        
        #usando o microfone
        with sr.Microphone() as source:
            
            #Chama um algoritmo de reducao de ruidos no som
            microfone.adjust_for_ambient_noise(source)
            
            #Frase para o usuario dizer algo
            print('Diga')
            #Armazena o que foi dito numa variavel
            audio = microfone.listen(source)
            
        try:
            #Passa a variável para o algoritmo reconhecedor de padroes
            frase = microfone.recognize_google(audio,language='pt-BR')
            
            #Retorna a frase pronunciada
            print("Você disse: " + frase)
            
            return self.escolha(frase)
            
        #Se nao reconheceu o padrao de fala, exibe a mensagem
        except sr.UnknownValueError:
            print("Não entendi")
            return self.microfone(0)
        
        

    #Funcao responsavel por falar 
    def criaaudio(self, audio):
        tts = gTTS(audio,lang='pt-br')
        a = str('audio.mp3')
        #Salva o arquivo de audio
        tts.save(a)
        mixer.init()
        mixer.music.load(a)
        mixer.music.play()
        while mixer.music.get_busy(): 
            time.Clock().tick(10)
        mixer.music.stop()
        mixer.music.load('a.mp3')
        os.remove(a)
    
    def verificar(self, email):
        is_valid = validate_email(email,check_mx=True, verify=True)

        if is_valid == True:
            return 1
        else:
            return 0


#telaself.tela()
#telaConectar()
#telaEsqSenha()
#telaself.tela()
#telaself.tela()
#root.mainloop()
if __name__ == "__main__":
    CadastroLogin('', '', '')