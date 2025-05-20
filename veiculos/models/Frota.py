

class Frota:
    def __init__(self, Veiculo):
        self.__frota = [Veiculo]

    def adicionar_veiculo(self, Veiculo):
        self.__frota.append(Veiculo)
    
    def listar_veiculos(self):
        print(self.__frota)

    def consumo_frota(self, distancia):
        consumo_total = 0
        for veiculo in self.__frota:
            consumo_total += veiculo.calcular_consumo(distancia)
        return consumo_total
