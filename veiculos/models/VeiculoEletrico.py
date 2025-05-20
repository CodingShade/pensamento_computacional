from .Veiculos import Veiculos

class VeiculoEletrico(Veiculos):
    def __init__(self, placa, modelo, marca, ano, cor, valor_fipe, nivel_bateria):
        super().__init__(placa, modelo, marca, ano, cor, valor_fipe)
        self.nivel_bateria = nivel_bateria

    def calcular_consumo(self, distancia):

        if distancia > 0:
            energia_gasta = distancia / 0.15
        else:
            energia_gasta = 0
        return energia_gasta
    
    def recarregar(self, nivel_bateria):
        """ Método para recarregar a bateria do veiculo eletrico
            Recebe o nivel da bateria em porcentagem.
            Se o nivel da bateria for maior que 100, retorna 100.
        """
        if nivel_bateria > 100:
            return 100
        else:
            return print(f"Nivel da bateria: {nivel_bateria}%")