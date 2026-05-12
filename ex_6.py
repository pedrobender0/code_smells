# Code Smell: Duplicated Code - processar_pagamento_credito e processar_pagamento_debito têm estruturas idênticas,
# diferindo apenas na taxa e no label.
# Solução: extrair a lógica para um metodo _processar_pagamento.

class ProcessadorFinanceiro:
    def processar_pagamento_credito(self, valor):
        self._processar_pagamento(valor, taxa=0.05, label="crédito")

    def processar_pagamento_debito(self, valor):
        self._processar_pagamento(valor, taxa=0.02, label="débito")

    def _processar_pagamento(self, valor, taxa, label):
        if valor > 0:
            valor_com_taxa = valor + (valor * taxa)
            print(f"Processando {label}: R$ {valor_com_taxa}")
        else:
            print("Valor inválido")