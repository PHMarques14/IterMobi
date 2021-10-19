from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from threading import Timer
from tkinter import *
from SGBD_IterMobi import *

class TelaMotorista:
    def __init__(self):
        self.telaSelecOnibus()
        
    def telaSelecOnibus(self):
        self.selecOnibus = Tk()
        self.selecOnibus.geometry("1280x720")
        self.selecOnibus['bg'] = "#cfcbcb"
        self.selecOnibus.title("IterMobi")
        self.img = PhotoImage(file="triangulos_appMotorista.png")
        self.img2 = PhotoImage(file="triangulos_appMotoristaInvertido.png")
        self.img3 = PhotoImage(file="logoProj.png")

        self.lblTri = Label(self.selecOnibus, image=self.img, bg="#cfcbcb")
        self.lblTri.place(x=-2,y=-1)
        
        self.lblTri2 = Label(self.selecOnibus, image=self.img2, bg="#cfcbcb")
        self.lblTri2.place(x=1136,y=-1)
        
        self.lblLogo3 = Label(self.selecOnibus, image=self.img3, bg="#cfcbcb")
        self.lblLogo3.place(x=200,y=70)
        
        self.lblLogo4 = Label(self.selecOnibus, image=self.img3, bg="#cfcbcb")
        self.lblLogo4.place(x=1000,y=70)

        texto = """CADASTRE A
LINHA DO ÔNIBUS"""

        self.mainLbl = Label(self.selecOnibus, text=texto, font="Helvetica 56 bold", bg = "#cfcbcb", fg = "#00226d")
        self.mainLbl.place(relx = 0.24,rely=0.1)
        self.lblLinha = Label(self.selecOnibus, text="NÚMERO DA LINHA", font="Arial 33", bg="#cfcbcb", fg = "#00226d")
        self.lblLinha.place(relx = 0.33, rely= 0.5)

        self.entryNumLinha = Entry(self.selecOnibus, relief = FLAT, font= "Helvetica 30", justify=CENTER)
        self.entryNumLinha.place(width=300,height=100,relx = 0.38, rely= 0.58)

        self.botaoConfirma = Button(self.selecOnibus, text="CONFIRMAR", font="Arial 33 bold", bg="#0f224b", fg = "#fff",relief = FLAT, activebackground="#6585cd", command=self.home)
        self.botaoConfirma.place(width=400,height=100,relx = 0.34, rely= 0.80)
        self.selecOnibus.mainloop()
    def home(self):
        texto = self.entryNumLinha.get()
        if texto == '':
            None
        else:
            self.entryNumLinha.destroy()
            self.botaoConfirma.destroy()
            self.lblTri.destroy()
            self.lblLogo4.destroy()

            self.lblLinha.config(text=texto, font="Helvetica 30 bold")
            self.lblLinha.place(relx=0.02, rely=0.1)
            self.mainLbl.config(text='IterMobi', font="Helvetica 30 bold")
            self.mainLbl.place(relx=0.02, rely=0.0)
            self.lblLogo3.place(x=200, y=0)

            self.atualizar()
    
    def atualizar(self):
        try:
            noti = open('noti.txt', 'r+')
            n = noti.read()
            noti.write('')
        except:
            n = ''
            pass
        if n == '':
            print('atualizando...')
            t = Timer(4, self.atualizar)
            t.start()
        else:
            nome = locNome(n)
            self.lblNoti = Label(self.selecOnibus, text=f'''UM PASSAGEIRO A CAMINHO:
{nome}''', font='Helvetica 25 bold', bg='#cfcbcb', bd=2, relief=GROOVE)
            self.lblNoti.place(relx=0.4, rely=0.05)

            nav = webdriver.Chrome('chromedriver.exe')

            cord = '-22.458704, -44.441193'
            link = f'https://www.google.com.br/maps/place/'+cord

            nav.get(link)

if __name__ == "__main__":
    TelaMotorista()