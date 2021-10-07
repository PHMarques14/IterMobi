from re import I
from SGBD_IterMobi import *
from tkinter import *
from threading import Timer
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from pygame import mixer
#from validate_email import validate_email

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
        self.img3 = PhotoImage(file="mic.png")

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
        self.entryConfSenha.bind('<Return>', self.home)
        self.btnConfirma = Button(self.tela, text="ENTRAR", font="Arial 11 bold", bg="#00226d", fg = "#fff",relief = FLAT, activebackground="#6585cd", command=lambda: self.home(0))
        self.btnConfirma.place(width=270,height=50,relx = 0.14, rely= 0.80)
        self.btnCadastroLogin = Label(self.tela, text="JÁ TEM CADASTRO? CLIQUE AQUI", font="Arial 9 underline", bg="#cfcbcb", fg = "#000", relief = FLAT)
        self.btnCadastroLogin.place(relx = 0.23, rely= 0.90)
        self.btnCadastroLogin.bind('<Button-1>', self.login)

        

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
        self.entrySenha.bind('<Return>', self.home)

        self.btnConfirma.configure(text="ENTRAR", font="Arial 11 bold", bg="#00226d", fg = "#fff",relief = FLAT, activebackground="#6585cd", command=lambda: self.home(1))
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
        self.btnConfirma.configure(text="ENVIAR", font="Arial 11 bold", bg="#00226d", fg = "#fff",relief = FLAT, activebackground="#6585cd", command=lambda: self.codigo(0))
        self.btnConfirma.place(width=270,height=50,relx = 0.14, rely= 0.80)
        self.btnConfirma.bind('<Return>', self.codigo)

    def codigo(self, event):
        '''Enivia um código ao e-mail inserido pelo usuário'''
        self.lblEmail.destroy()
        self.entryEmail.destroy()

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
        self.entryCodigo.bind('<Return>', self.alterar)
        self.btnConfirma.configure(command=lambda: self.alterar(0))

        self.btnReenvia = Button(self.tela, text="REENVIAR CÓDIGO", font="Arial 11 bold", bg="#6585cd", fg = "#fff",relief = FLAT, activebackground="#6585cd")
        self.btnReenvia.place(width=230,height=40,relx = 0.2, rely= 0.64)

    def alterar(self, event):
        '''Altera a senha antiga da conta do usuário e insere uma nova senha ao banco de dados'''
        self.infoLbl.destroy()
        self.lblCodigo.destroy()
        self.entryCodigo.destroy()
        self.btnReenvia.destroy()

        self.texto = """ESQUECEU A
        SENHA?"""

        self.mainLbl.configure(text=self.texto, font="Helvetica 23 bold", bg = "#cfcbcb", fg = "#00226d")
        self.mainLbl.place(relx = 0.24,rely=0.1)
        self.lblSenha = Label(self.tela, text="SENHA", font="Arial 11", bg="#cfcbcb", fg = "black")
        self.lblSenha.place(relx = 0.14, rely= 0.32)
        self.lblRepeteSenha = Label(self.tela, text="REPITA SUA NOVA SENHA", font="Arial 11", bg="#cfcbcb", fg = "black")
        self.lblRepeteSenha.place(relx = 0.14, rely= 0.47)

        self.entrySenha = Entry(self.tela, relief = FLAT, font= "Helvetica 11")
        self.entrySenha.place(width=270,height=50,relx = 0.14, rely= 0.36)
        self.entryRepeteSenha = Entry(self.tela, relief = FLAT, font= "Helvetica 11")
        self.entryRepeteSenha.place(width=270,height=50,relx = 0.14, rely= 0.5)
        
        self.btnConfirma.configure(text="CONFIRMAR", font="Arial 11 bold", bg="#00226d", fg = "#fff",relief = FLAT, activebackground="#6585cd")
        self.btnConfirma.place(width=270,height=50,relx = 0.14, rely= 0.80)
    
    def enviarcodigo(email):
        cod = randint(1, 999999)
        senha = open('senha.txt', 'r')

        to = email
        user = 'emanulucio@gmail.com'
        smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo
        smtpserver.login(user, senha.read())
        msg = f'''
Olá querido usuário!

Aqui está o código para trocar sua senha: {cod}. Para trocá-la, basta estar no aplicativo e digitar esse código no espaço determinado.

Atenciosamente,
Equipe IterMobi'''
        smtpserver.sendmail(user, to, msg)
        print('done!')
        smtpserver.close()

        return cod  
        
    def home(self, event):
        self.nomeUsuario = self.entryNome.get()
        self.emailUsuario = self.entryEmail.get()
        self.senha = self.entrySenha.get()
        self.confSenha = self.entryConfSenha.get()

        #is_valid = validate_email('emanulucio@gmail.com')
        #is_valid = validate_email('emanulucio@gmail.com',check_mx=True)
        #is_valid = validate_email('emanulucio@gmail.com',verify=True)

        if self.nomeUsuario == '' :
            None
        elif self.emailUsuario == '':
            None
        elif self.senha == '':
            None
        elif self.confSenha == '':
            None
        #elif is_valid == False:
        #    None
        else:
            self.mainLbl.configure(text="Seja bem-vindo!", font="Beirut 28", bg = "#cfcbcb", fg = "#30343F")
            self.mainLbl.place(relx = 0.02,rely=0.03)
            self.lblBusca = Label(self.tela, bg = "#00226d")
            self.lblBusca.place(width=400,height=66,relx = 0, rely= 0.12)
            self.entryBusca = Entry(self.lblBusca, relief = FLAT, font= "Helvetica 14")
            self.entryBusca.place(width=309,height=54,relx = 0.01, rely= 0.05)

            self.lblMic = Button(self.tela, image=self.img3, command=self.microfone)
            self.lblMic.place(x=315,y=86)

            self.lblLugRec = Label(self.tela, text="Lugares recentes:", font="Beirut 18", bg = "#cfcbcb", fg = "#5E5E5E")
            self.lblLugRec.place(relx = 0.02, rely=0.34)
            
            self.lblSelec = Label(self.tela)
            self.lblSelec.place(width=400,height=240,relx = 0, rely=0.4)

            self.lblPLugar = Label(self.lblSelec, text="Graal Resende", font="Beirut 18", bg = "#2955b6", fg = "white", anchor= "nw")
            self.lblPLugar.place(width=400,height=80,x= -2, y = -2)
            self.lblPLugarEnder = Label(self.lblSelec, text="Graal Resende", font="Beirut 18", bg = "#2955b6", fg = "white", anchor= "nw")
            self.lblPLugarEnder.place(width=400,height=80,x= -2, y = -2)
            self.lblSLugar = Label(self.lblSelec, text="Rodoviária Velha", font="Beirut 18", bg = "#160b7d", fg = "white", anchor= "nw")
            self.lblSLugar.place(width=400,height=80,x= -2, y = 78)
            self.lblTLugar = Label(self.lblSelec, text="Av. Perimetral Norte, 609", font="Beirut 18", bg = "#6585cd", fg = "white", anchor= "nw")
            self.lblTLugar.place(width=400,height=80,x= -2, y = 158)

    def microfone(self):
        #Função para ouvir e reconhecer a fala
        #Habilita o microfone do usuário
        microfone = sr.Recognizer()
        
        #usando o microfone
        with sr.Microphone() as source:
            
            #Chama um algoritmo de reducao de ruidos no som
            microfone.adjust_for_ambient_noise(source)
            
            #Frase para o usuario dizer algo
            
            #Armazena o que foi dito numa variavel
            audio = microfone.listen(source)
            
        try:
            
            #Passa a variável para o algoritmo reconhecedor de padroes
            frase = microfone.recognize_google(audio,language='pt-BR')
            
            #Retorna a frase pronunciada
            print("Você disse: " + frase)
            self.cria_audio(frase)
            
        #Se nao reconheceu o padrao de fala, exibe a mensagem
        except sr.UnknownValueError:
            print("Não entendi")
            return self.microfone()
        
        return frase

    #Funcao responsavel por falar 
    def cria_audio(self, audio):
        tts = gTTS(audio,lang='pt-br')
        a = str('audio.mp3')
        #Salva o arquivo de audio
        tts.save(a)
        mixer.init()
        mixer.music.load(a)
        mixer.music.play()
        while mixer.music.get_busy(): 
            mixer.time.Clock().tick(10)
        os.remove(mp3file)
        
        #ouvir_microfone()
        #print('ok agora')

#telaself.tela()
#telaConectar()
#telaEsqSenha()
#telaself.tela()
#telaself.tela()
#root.mainloop()
if __name__ == "__main__":
    CadastroLogin('', '', '')