# Code Smell: Switch Statements - A cadeia de if/elif repetia a mesma verificação de tipo
# Solução: substituir os condicionais por um dicionário de tarifas com constantes nomeadas.

tarifas_frete = {
    "MOTO":      {"taxa_km": 2.0,  "taxa_base": 0.0},
    "CARRO":     {"taxa_km": 3.5,  "taxa_base": 10.0},
    "CAMINHAO":  {"taxa_km": 8.0,  "taxa_base": 50.0},
    "BICICLETA": {"taxa_km": 1.0,  "taxa_base": 0.0},
}

class CalculadoraDeFrete:
    def calcular_frete(self, tipo_transporte, distancia):
        if tipo_transporte not in tarifas_frete:
            raise ValueError("Tipo de transporte desconhecido")
        tarifa = tarifas_frete[tipo_transporte]
        return distancia * tarifa["taxa_km"] + tarifa["taxa_base"]