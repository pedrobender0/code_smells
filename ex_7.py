# Code Smell: Message Chain - pedido.cliente.endereco.estado.pais.nome acaba criando um acoplamento excessivo entre classes.
# Solução: adicionar o metodo get_pais_destino() em Cliente e Pedido

class Pais:
    def __init__(self, nome):
        self.nome = nome

class Estado:
    def __init__(self, nome, pais):
        self.nome = nome
        self.pais = pais

class Endereco:
    def __init__(self, rua, estado):
        self.rua = rua
        self.estado = estado

class Cliente:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def get_pais_destino(self):
        return self.endereco.estado.pais.nome

class Pedido:
    def __init__(self, cliente, valor):
        self.cliente = cliente
        self.valor = valor

    def get_pais_destino(self):
        return self.cliente.get_pais_destino()

def verificar_frete_internacional(pedido: Pedido):
    pais_destino = pedido.get_pais_destino()
    if pais_destino != "Brasil":
        print("Sujeito a taxa de importação.")
    else:
        print("Frete nacional padrão.")