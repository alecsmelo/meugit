class Imprimir:
    def __init__(self, vl1, vl2):
        self.valor1 = vl1
        self.valor2 = vl2
    def calcular(self):
        self.resultado = self.valor1 + self.valor2
        print("Resultado: " + str(self.resultado))

Valores = Imprimir(135,1263)
print("Valor 1 Cadastrado: " + str(Valores.valor1))
print("Valor 2 Cadastrado: " + str(Valores.valor2))

Valores.calcular()