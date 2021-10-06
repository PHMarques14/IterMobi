<<<<<<< HEAD
from tkinter import *

def telaSejaBV(self):
    self.tela = Tk()
    self.tela.geometry("375x677")
    self.tela['bg'] = "#cfcbcb"
    self.tela.title("IterMobi")

    self.mainLbl = Label(self.tela, text="Seja bem-vindo!", font="Beirut 28", bg = "#cfcbcb", fg = "#30343F")
    self.mainLbl.place(relx = 0.02,rely=0.03)
    self.lblBusca = Label(self.tela, bg = "#00226d")
    self.lblBusca.place(width=400,height=66,relx = 0, rely= 0.12)
    self.entryBusca = Entry(self.lblBusca, relief = FLAT, font= "Helvetica 14")
    self.entryBusca.place(width=309,height=54,relx = 0.01, rely= 0.05)

    self.img = PhotoImage(file="iconeMic.png")

    self.lblMic = Label(self.tela, image=self.img)
    self.lblMic.place(x=315,y=86)

    self.lblLugRec = Label(self.tela, text="Lugares recentes:", font="Beirut 18", bg = "#cfcbcb", fg = "#5E5E5E")
    self.lblLugRec.place(relx = 0.02, rely=0.34)
    
    self.lblSelec = Label(self.tela)
    self.lblSelec.place(width=400,height=240,relx = 0, rely=0.4)

    self.lblPLugar = Label(self.lblSelec, text="Graal Resende", font="Beirut 18", bg = "#2955b6", fg = "white", anchor= "nw")
    self.lblPLugar.place(width=400,height=80,x= -2, y = -2)
    self.lblPLugarEnder = Label(self.lblSelec, text="Rodovia Presidente Dutra, Paraíso", font="Beirut 12", bg = "#2955b6", fg = "#bababa", anchor= "w")
    self.lblPLugarEnder.place(x= -2, y = 50)

    self.lblSLugar = Label(self.lblSelec, text="Rodoviária Velha", font="Beirut 18", bg = "#160b7d", fg = "white", anchor= "nw")
    self.lblSLugar.place(width=400,height=80,x= -2, y = 78)
    self.lblSLugarEnder = Label(self.lblSelec, text="R. Pintor Nunes de Paula, 137, Centro", font="Beirut 12", bg = "#160b7d", fg = "#bababa", anchor= "w")
    self.lblSLugarEnder.place(x= -2, y = 120)

    self.lblTLugar = Label(self.lblSelec, text="Av. Perimetral Norte, 609", font="Beirut 18", bg = "#6585cd", fg = "white", anchor= "nw")
    self.lblTLugar.place(width=400,height=80,x= -2, y = 158)
    self.lblPLugarEnder = Label(self.lblSelec, text="Av. Perimetral Norte, 609, Cidade Alegria", font="Beirut 12", bg = "#6585cd", fg = "#bababa", anchor= "w")
    self.lblPLugarEnder.place(x= -2, y = 200)
=======
from tkinter import *

def telaSejaBV():
    tela = Tk()
    tela.geometry("375x677")
    tela['bg'] = "#cfcbcb"
    tela.title("IterMobi")

    mainLbl = Label(tela, text="Seja bem-vindo!", font="Beirut 28", bg = "#cfcbcb", fg = "#30343F")
    mainLbl.place(relx = 0.02,rely=0.03)
    lblBusca = Label(tela, bg = "#00226d")
    lblBusca.place(width=400,height=66,relx = 0, rely= 0.12)
    entryBusca = Entry(lblBusca, relief = FLAT, font= "Helvetica 14")
    entryBusca.place(width=309,height=54,relx = 0.01, rely= 0.05)

    img = PhotoImage(file="iconeMic.png")

    lblMic = Label(tela, image=img)
    lblMic.place(x=315,y=86)

    lblLugRec = Label(tela, text="Lugares recentes:", font="Beirut 18", bg = "#cfcbcb", fg = "#5E5E5E")
    lblLugRec.place(relx = 0.02, rely=0.34)
    
    lblSelec = Label(tela)
    lblSelec.place(width=400,height=240,relx = 0, rely=0.4)

    lblPLugar = Label(lblSelec, text="Graal Resende", font="Beirut 18", bg = "#2955b6", fg = "white", anchor= "nw")
    lblPLugar.place(width=400,height=80,x= -2, y = -2)
    lblPLugarEnder = Label(lblSelec, text="Graal Resende", font="Beirut 18", bg = "#2955b6", fg = "white", anchor= "nw")
    lblPLugarEnder.place(width=400,height=80,x= -2, y = -2)
    lblSLugar = Label(lblSelec, text="Rodoviária Velha", font="Beirut 18", bg = "#160b7d", fg = "white", anchor= "nw")
    lblSLugar.place(width=400,height=80,x= -2, y = 78)
    lblTLugar = Label(lblSelec, text="Av. Perimetral Norte, 609", font="Beirut 18", bg = "#6585cd", fg = "white", anchor= "nw")
    lblTLugar.place(width=400,height=80,x= -2, y = 158)











    tela.mainloop()

telaSejaBV()
>>>>>>> 443b066c952046670e001bb6f25a62af8f4790fa
