from tkinter import *

def telaSejaBV():
    tela = Tk()
    tela.geometry("375x677")
    tela['bg'] = "#cfcbcb"
    tela.title("IterMobi")

    mainLbl = Label(tela, text="SEJA BEM-VINDO!", font="Beirut 28", bg = "#cfcbcb", fg = "#30343F")
    mainLbl.place(relx = 0.06,rely=0.03)
    lblBusca = Label(tela, bg = "#00226d")
    lblBusca.place(width=400,height=66,relx = 0, rely= 0.12)
    entryBusca = Entry(lblBusca, relief = FLAT, font= "Helvetica 14")
    entryBusca.place(width=300,height=50,relx = 0.01, rely= 0.1)

    img = PhotoImage(file="iconeMic.png")

    lblMic = Label(tela, image=img, bg="#cfcbcb")
    lblMic.place(x=310,y=85)

























    tela.mainloop()

telaSejaBV()