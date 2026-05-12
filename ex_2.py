# Code Smell: Long Parameter List + Data Clumps
# A classe funcionário recebe 11 parâmetros, e os grupos de dados endereço e telefone,
# que são relacionados, estavam soltos como parâmetros avulsos.
# Solução: criar classes Endereco e Telefone.

class Endereco:
    def __init__(self, rua, numero, bairro, cidade, estado, cep):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep

class Telefone:
    def __init__(self, ddd, numero):
        self.ddd = ddd
        self.numero = numero

class Funcionario:
    def __init__(self, nome, cargo, salario, endereco: Endereco, telefone: Telefone):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.endereco = endereco
        self.telefone = telefone

    def exibir_dados(self):
        print(f"Funcionario: {self.nome} - {self.cargo}")
        print(f"Contato: ({self.telefone.ddd}) {self.telefone.numero}")
        e = self.endereco
        print(f"Endereço: {e.rua}, {e.numero} - {e.bairro}, {e.cidade}/{e.estado} - CEP: {e.cep}")