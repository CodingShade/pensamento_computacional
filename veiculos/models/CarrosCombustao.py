from .Veiculos import Veiculos

class CarrosCombustao(Veiculos):
    def __init__(self, placa, modelo, marca, cor, ano, valor_fipe, combustivel, n_portas, n_assentos, n_cilindrada, n_cambio) -> None:
        
        super().__init__(placa, modelo, marca, cor, ano, valor_fipe)

        self.__combustivel = combustivel
        self.__n_portas = n_portas
        self.__n_assentos = n_assentos
        self.__n_cilindrada = n_cilindrada
        self.__n_cambio = n_cambio

    def __str__(self):
        infos =  super().__str__()
        infos += f"Combustivel: {self.__combustivel}\n"
        infos += f"Numero de portas: {self.__n_portas}\n"
        infos += f"Numero de assentos: {self.__n_assentos}\n"
        infos += f"Numero de cilindradas: {self.__n_cilindrada}\n"
        infos += f"Numero de cambios: {self.__n_cambio}\n"
        
        return infos