import pandas as pd

def PesquisaPlaca():
    data = pd.read_csv('Medidas_Placas.CSV', sep=';')
    Qplaca = input("Terreno + Tabuletas (000A + 000B): ")
    Qpraca = input("Praça (JP/PE/CG): ")

    try:
        FiltraPlaca=data.loc[(data['ID'] == Qplaca) & (data['PRACA'] == Qpraca)]
    except:
        print("Placa não Localizada")
    finally:
        print(FiltraPlaca)

PesquisaPlaca()