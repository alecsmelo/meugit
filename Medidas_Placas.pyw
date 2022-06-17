import pandas as pd
from tkinter import *

Janela = Tk()
Janela.title("Pesquisa Placa")
Janela.geometry('300x100')

def PesquisaPlaca():
    data = pd.read_csv('Medidas_Placas.CSV', sep=';')
    Qplaca = Entrada.get()
    Qpraca = Entrada1.get()

    try:
        FiltraPlaca=data.loc[(data['ID'] == Qplaca) & (data['PRACA'] == Qpraca)]
    except:
        print("Placa não Localizada")
    finally:
        Label3.configure(text=FiltraPlaca)

Label1 = Label(Janela, text="Digite a Placa")
Label1.place(x=15, y=5)
Entrada = Entry(Janela, width=12)
Entrada.place(x=15, y=25)

Label2 = Label(Janela, text="Digite a Praça")
Label2.place(x=15, y=45)
Entrada1 = Entry(Janela, width=12)
Entrada1.place(x=15, y=65)

Label3 = Label(Janela, text="Placa e Medidas")
Label3.place(x=100, y=14)

Botao = Button(Janela, text="Procurar", command=PesquisaPlaca)
Botao.place(x=165, y=65)


Janela.mainloop()
