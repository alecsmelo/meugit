class Cadastro():
    def __init__(self, Nome, Cargo, Turno, Salario):
        self.Nome = Nome
        self.Cargo = Cargo
        self.Turno = Turno
        self.Salario = Salario

    def ExibirCasdastro(self):
        amount = self.Salario
        thousands_separator = "."
        fractional_separator = ","

        currency = "R${:,.2f}".format(amount)

        if thousands_separator == ".":
            main_currency, fractional_currency = currency.split(".")[0], currency.split(".")[1]
            new_main_currency = main_currency.replace(",", ".")
            currency = new_main_currency + fractional_separator + fractional_currency

        print("Funcionário: " + self.Nome)
        print("Cargo: " + self.Cargo)
        print("Turno: " + self.Turno)
        print("Salário: " + str(currency))

CadFunc = input("Digite Nome do Funcionário: ")
CadCargo = input("Digite o Cargo do Funcionário: ")
CadTurno = input("Digite o Horário: ")
CadSalario = float(input("Digite o Salário: "))

CadFunc = Cadastro(CadFunc, CadCargo, CadTurno, CadSalario)
print("")
CadFunc.ExibirCasdastro()







