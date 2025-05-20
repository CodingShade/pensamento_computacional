import re

class Veiculos:
    """
    Classe com as principais funcionalidades do sistema de veiculos, como placas, veiculos, etc.
    """

    def __init__( self, placa: str, modelo: str, marca: str, ano: int, cor: str, valor_fipe: float) -> None:
        """Construtor da classe Veiculo"""
        self.__placa = placa
        self.__modelo = modelo
        self.__marca = marca
        self.__ano = ano
        self.__cor = cor
        self.__valor_fipe = valor_fipe

    def __str__(self) -> str:
        """Retorna uma string com as informações do veiculo"""
        infos = f"Placa: {self.__placa}\n"
        infos += f"Modelo: {self.__modelo}\n"
        infos += f"Marca: {self.__marca}\n"
        infos += f"Ano: {self.__ano}\n"
        infos += f"Cor: {self.__cor}\n"
        infos += f"Valor Fipe: {self.__valor_fipe}\n"
        return infos

    def getPlaca(self) -> str:
        """Retorna a placa do veiculo"""
        return self.__placa
    
    def get_placa(self) -> str:
        """Retorna a placa do veículo"""
        return self.__placa

    def set_placa(self, placa: str) -> bool:
        """Método que altera a placa do Veículo, se seguir o padrão brasileiro (3 letras e 4 números)
        Argumento: placa (str): nova placa
        Saída: True se a placa for válida e alterada, False caso contrário
        """
        padrao_placa = r'^[A-Z]{3}[0-9]{4}$'
        if re.match(padrao_placa, placa):
            self.__placa = placa
            return True
        return False

    def setValorFipe(self, valor: float) -> None:
        """Método que altera o valor da Fipe do Veículo

        Argumento: valor (float): novo valor da Fipe
        Saída: True se ok
        """
        self.__valor_fipe = valor
        return True
    
    def calcular_consumo(distancia: float):
        """ Método para calcular o consumo de uma distancia determinada.
            Recebe a distancia em km.
            calculo: distancia recebida / eficacia do transporte = litros gastos
        """
        pass
        
    def __eq__(self, other):
        """Compara dois veículos pela placa"""
        if isinstance(other, Veiculos):
            return self.__placa == other.__placa
        return False


    