class Cadastro():
    def __init__(self, Nome, Cargo, Turno, Salario):
        self.Nome = Nome
        self.Cargo = Cargo
        self.Turno = Turno
        self.Salario = float(Salario)

    def ExibirCasdastro(self):
        Salario_BRL = "R${:,.2f}".format(self.Salario).replace(",","X").replace(".",",").replace("X",".")
        print("Funcionário: " + self.Nome)
        print("Cargo: " + self.Cargo)
        print("Turno: " + self.Turno)
        print("Salário: " + str(Salario_BRL))

CadNome = input("Digite Nome do Funcionário: ")
CadCargo = input("Digite o Cargo do Funcionário: ")
CadTurno = input("Digite o Horário: ")
CadSalario = input("Digite o Salário: ")

CadFunc = Cadastro(CadNome, CadCargo, CadTurno, CadSalario)
CadFunc.ExibirCasdastro()







