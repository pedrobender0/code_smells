# Code Smell: Long Parameter List - A função recebia 9 parâmetros
# Solução: agrupar dados em classes Hospede e Quarto

taxa_cafe_da_manha = 50

class Hospede:
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email

class Quarto:
    def __init__(self, numero, tipo):
        self.numero = numero
        self.tipo = tipo

def criar_reserva(hospede: Hospede, quarto: Quarto, data_checkin, data_checkout, valor_diaria, possui_cafe_da_manha):
    print(f"Reserva criada para {hospede.nome} (CPF: {hospede.cpf})")
    print(f"Quarto {quarto.numero} ({quarto.tipo})")
    print(f"De {data_checkin} até {data_checkout}")
    total_dias = (data_checkout - data_checkin).days
    total = total_dias * valor_diaria
    if possui_cafe_da_manha:
        total += taxa_cafe_da_manha * total_dias
    print(f"Total a pagar: R$ {total}")