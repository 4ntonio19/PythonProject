from tkinter import *
janela = Tk()
janela.geometry("1440x1024")
janela.title("Tela de reservas")

rotuloDoTitulo = Label(janela, bg="dark blue", width=125, height=6)
rotuloDoTitulo.pack()

titulo1 = Label(janela, text="Wyden Hotel", font=("Wyden Hotel", 20), bg="dark blue", fg="white")
titulo1.pack()
titulo1.place(x=300, y=40)

titulo2 = Label(janela, text="Quartos:", font=("Quartos", 18))
titulo2.pack()
#----------------------------------------------------------------------------------------------
caixa1A = Label(janela, bg="green3", width=12, height=5)
caixa1A.pack()
caixa1A.place(x=475, y=150)

caixa1B = Label(janela, bg="green3", width=12, height=5)
caixa1B.pack()
caixa1B.place(x=600, y=150)

caixa1C = Label(janela, bg="red", width=12, height=5)
caixa1C.pack()
caixa1C.place(x=725, y=150)

caixa1D = Label(janela, bg="green3", width=12, height=5)
caixa1D.pack()
caixa1D.place(x=850, y=150)
#-----------------------------------------------------------------------------------------------------------
caixa2A = Label(janela, bg="green3", width=12, height=5)
caixa2A.pack()
caixa2A.place(x=475, y=250)

caixa2B = Label(janela, bg="red", width=12, height=5)
caixa2B.pack()
caixa2B.place(x=600, y=250)

caixa2C = Label(janela, bg="red", width=12, height=5)
caixa2C.pack()
caixa2C.place(x=725, y=250)

caixa2D = Label(janela, bg="green3", width=12, height=5)
caixa2D.pack()
caixa2D.place(x=850, y=250)
#------------------------------------------------------------------------------------------------------------
caixa3A = Label(janela, bg="red", width=12, height=5)
caixa3A.pack()
caixa3A.place(x=475, y=350)

caixa3B = Label(janela, bg="red", width=12, height=5)
caixa3B.pack()
caixa3B.place(x=600, y=350)

caixa3C = Label(janela, bg="green3", width=12, height=5)
caixa3C.pack()
caixa3C.place(x=725, y=350)

caixa3D = Label(janela, bg="red", width=12, height=5)
caixa3D.pack()
caixa3D.place(x=850, y=350)
#-------------------------------------------------------------------------------------------------------------
caixa4A = Label(janela, bg="red", width=12, height=5)
caixa4A.pack()
caixa4A.place(x=475, y=450)

caixa4B = Label(janela, bg="green3", width=12, height=5)
caixa4B.pack()
caixa4B.place(x=600, y=450)

caixa4C = Label(janela, bg="red", width=12, height=5)
caixa4C.pack()
caixa4C.place(x=725, y=450)

caixa4D = Label(janela, bg="green3", width=12, height=5)
caixa4D.pack()
caixa4D.place(x=850, y=450)
#---------------------------------------------------------------------------------------------------
caixa5A = Label(janela, bg="red", width=12, height=5)
caixa5A.pack()
caixa5A.place(x=475, y=550)

caixa5B = Label(janela, bg="green3", width=12, height=5)
caixa5B.pack()
caixa5B.place(x=600, y=550)

caixa5C = Label(janela, bg="red", width=12, height=5)
caixa5C.pack()
caixa5C.place(x=725, y=550)

caixa5D = Label(janela, bg="red", width=12, height=5)
caixa5D.pack()
caixa5D.place(x=850, y=550)


janela.mainloop()