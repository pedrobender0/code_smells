# Code Smell: God Class/Violação SRP - A classe Produto acumula três responsabilidades diferentes:
# cálculo de imposto, persistência em banco de dados e exportação XML.
# Solução: separar em três classes — Produto, ProdutoRepository e ProdutoSerializer.

class Produto:
    def __init__(self, id_produto, nome, preco):
        self.id_produto = id_produto
        self.nome = nome
        self.preco = preco

    def calcular_preco_com_imposto(self):
        return self.preco * 1.15


class ProdutoRepository:
    def salvar(self, produto: Produto):
        print(f"INSERT INTO produtos (id, nome, preco) VALUES ({produto.id_produto}, '{produto.nome}', {produto.preco});")


class ProdutoSerializer:
    def exportar_para_xml(self, produto: Produto):
        return (f"<produto><id>{produto.id_produto}</id>"
                f"<nome>{produto.nome}</nome>"
                f"<preco>{produto.preco}</preco></produto>")