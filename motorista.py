from tkinter import *

class TelaMotorista:
    def __init__(self):
        self.telaSelecOnibus()
        
    def telaSelecOnibus(self):
        self.selecOnibus = Tk()
        self.selecOnibus.geometry("1280x720")
        self.selecOnibus['bg'] = "#cfcbcb"
        self.selecOnibus.title("IterMobi")
        img = PhotoImage(file="triangulos_appMotorista.png")
        img2 = PhotoImage(file="triangulos_appMotoristaInvertido.png")

        lblTri = Label(self.selecOnibus, image=img, bg="#cfcbcb")
        lblTri.place(x=-2,y=-1)
        
        lblTri2 = Label(self.selecOnibus, image=img2, bg="#cfcbcb")
        lblTri2.place(x=1136,y=-1)

        img3 = PhotoImage(file="logoProj.png")

        lblTri3 = Label(self.selecOnibus, image=img3, bg="#cfcbcb")
        lblTri3.place(x=200,y=70)
        
        lblTri3 = Label(self.selecOnibus, image=img3, bg="#cfcbcb")
        lblTri3.place(x=1000,y=70)

        texto = """CADASTRE A
LINHA DO ÔNIBUS"""

        mainLbl = Label(self.selecOnibus, text=texto, font="Helvetica 56 bold", bg = "#cfcbcb", fg = "#00226d")
        mainLbl.place(relx = 0.24,rely=0.1)
        lblLinha = Label(self.selecOnibus, text="NÚMERO DA LINHA", font="Arial 33", bg="#cfcbcb", fg = "#00226d")
        lblLinha.place(relx = 0.33, rely= 0.5)

        entryNumLinha = Entry(self.selecOnibus, relief = FLAT, font= "Helvetica 30", justify=CENTER)
        entryNumLinha.place(width=300,height=100,relx = 0.38, rely= 0.58)

        botaoConfirma = Button(self.selecOnibus, text="CONFIRMAR", font="Arial 33 bold", bg="#0f224b", fg = "#fff",relief = FLAT, activebackground="#6585cd")
        botaoConfirma.place(width=400,height=100,relx = 0.34, rely= 0.80)
        self.selecOnibus.mainloop()

if __name__ == "__main__":
    TelaMotorista()