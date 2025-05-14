class Veiculos:
    '''
    Classe com as principais funcionalidades do sistema de veiculos, como placa
    '''
    def __init__(self, placa: str, modelo: str, marca: str, cor: str, ano: int, valor_fipe: float):
        self.__placa = placa
        self.__modelo = modelo
        self.__marca = marca
        self.__cor = cor
        self.__ano = ano
        self.__valor_fipe = valor_fipe

    def __str__(self) -> str:
        infos = f"Placa: {self.__placa}\n"
        infos += f"Modelo: {self.__modelo}\n"
        infos += f"Marca: {self.__marca}\n"
        infos += f"Cor: {self.__cor}\n"
        infos += f"Ano: {self.__ano}\n"
        infos += f"Valor fipe: {self.__valor_fipe}"
        return infos