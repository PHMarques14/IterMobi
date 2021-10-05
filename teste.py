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
    lblSLugar = Label(lblSelec, text="Rodoviária Velha", font="Beirut 18", bg = "#160b7d", fg = "white", anchor= "nw")
    lblSLugar.place(width=400,height=80,x= -2, y = 78)
    lblTLugar = Label(lblSelec, text="Av. Perimetral Norte, 609", font="Beirut 18", bg = "#6585cd", fg = "white", anchor= "nw")
    lblTLugar.place(width=400,height=80,x= -2, y = 158)











    tela.mainloop()

telaSejaBV()