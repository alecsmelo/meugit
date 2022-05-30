class Imprimir:
    def __init__(self, vl1, vl2):
        self.valor1 = vl1
        self.valor2 = vl2
    def calcular(self):
        self.resultado = self.valor1 + self.valor2
        print("Resultado: " + str(self.resultado))

Entrada1 = int(input("Digite o Valor: "))
Endrada2 = int(input("Digite o segundo valor: "))

Cadastro = Imprimir(Entrada1,Endrada2)
print("Valor 1 Cadastrado: " + str(Cadastro.valor1))
print("Valor 2 Cadastrado: " + str(Cadastro.valor2))

Cadastro.calcular()