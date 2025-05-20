from .Veiculos import Veiculos

class Carro(Veiculos):
    def __init__(self, placa, modelo, marca, ano, cor, valor_fipe):
        super().__init__(placa, modelo, marca, ano, cor, valor_fipe)

    def calcular_consumo(self, distancia):

        if distancia > 0:
            litro_gasto = distancia / 12
        else:
            litro_gasto = 0
        return litro_gasto

            