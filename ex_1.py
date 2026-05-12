#Smell: O metodo processar_venda_e_gerar_relatorio faz muitas coisas, como calcular total,
#aplicar desconto, processar pagamento e gerar relatório e isso viola o Single
#Responsibility Principle.
#Solução: Dividir em diferentes métodos cada ação

class GerenciadorDeVendas:
    def processar_venda(self, itens, cliente, metodo_pagamento):
        total = self._calcular_total(itens)
        total = self._aplicar_desconto(total, cliente)
        self._processar_pagamento(total, metodo_pagamento)
        self._gerar_relatorio(total, cliente)
        print("Venda processada com sucesso.")

    def _calcular_total(self, itens):
        return sum(item['preco'] * item['quantidade'] for item in itens)

    def _aplicar_desconto(self, total, cliente):
        if cliente['tipo'] == 'VIP':
            return total * 0.90
        return total

    def _processar_pagamento(self, total, metodo_pagamento):
        if metodo_pagamento == 'CARTAO':
            print(f"Cobrando R$ {total} no cartão de crédito...")
        elif metodo_pagamento == 'BOLETO':
            print(f"Gerando boleto no valor de R$ {total}...")

    def _gerar_relatorio(self, total, cliente):
        relatorio = f"--- Relatório de Venda ---\nCliente: {cliente['nome']}\nTotal: R$ {total}\n"
        with open("relatorio_vendas.txt", "a") as f:
            f.write(relatorio)
