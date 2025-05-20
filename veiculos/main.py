# Importando as classes necessárias
from models.Veiculos import Veiculos
from models.CarroCombustao import CarroCombustao
from models.CarroEletrico import CarroEletrico
from models.CarroConvEletrico import CarroConvEletrico
from models.Carro import Carro
from models.Moto import Moto
from models.Caminhao import Caminhao
from models.Frota import Frota
from models.VeiculoEletrico import VeiculoEletrico

# Criando instâncias de cada classe
voyage = Veiculos("BCE9D36", "Voyage", "Volkswagen", 2018, "Vermelho", 47793)

# Criando um carro a combustão
jetta_gli = CarroCombustao(placa="JDM9D36",
                           modelo="Jetta GLI",
                           marca="Volkswagen",
                           ano=2025,
                           cor="Vermelho",
                           valor_fipe=250000,
                           combustivel="Gasolina",
                           nPortas=4,
                           nAssentos=5,
                           nCilindrada=2000,
                           nCambio="AT 7",
                           nivel_combustivel=24)

# Criando um carro elétrico
tesla_model_s = CarroEletrico(placa="JDN0A00",
                              modelo="Tesla Model S",
                              marca="Tesla",
                              ano=2021,
                              cor="Branco",
                              valor_fipe=950000,
                              nAssentos=5,
                              nPortas=4,
                              nivel_bateria=65,
                              tipo_bateria="Lítio",
                              autonomia=491)

# Criando um carro convertido em elétrico (combustão + elétrico)
# (herança múltipla)
fusca_eletrico = CarroConvEletrico(placa="IAA0D36",
                                   modelo="Fusca 1600 Elétrico",
                                   marca="Volkswagen",
                                   ano=1975,
                                   cor="Azul",
                                   valor_fipe=70000,
                                   combustivel="Gasolina",
                                   nPortas=4,
                                   nAssentos=5,
                                   nCilindrada=1600,
                                   nCambio="MT 4",
                                   nivel_combustivel=24,
                                   tipo_bateria="Lítio",
                                   autonomia=150,
                                   nivel_bateria=65)

#lista para testar o metodo calcular_consumo


# Exibindo as informações dos veículos
print("Informações dos veículos: ")
print("\n\n######## Veículo: #########")
print(voyage)
print("\n\n######## Carro a combustão: #########")
print(jetta_gli)
print("\n\n######## Carro elétrico: #########")
print(tesla_model_s)
print("\n\n######## Carro convertido em elétrico: #########")
print(fusca_eletrico)
# Abastecendo o carro a combustão
jetta_gli.abastecer(10)
print(jetta_gli)
# Abastecendo o carro convertido em elétrico
fusca_eletrico.abastecer(10)
# Exibindo as informações do carro convertido em elétrico
print("\n\n######## Carro conv. elétrico após abastecimento: #########")
print(fusca_eletrico)

distancia = float(input("Digite a distancia:"))


gol = Carro(placa="JDM9D36",
                           modelo="Jetta GLI",
                           marca="Volkswagen",
                           ano=2025,
                           cor="Vermelho",
                           valor_fipe=250000)

cg_125 = Moto(placa="JDM9D36",
                           modelo="cg_125",
                           marca="Honda",
                           ano=2025,
                           cor="Amarelo",
                           valor_fipe=100000)

fh = Caminhao(placa="JDM9D36",
                           modelo="FH",
                           marca="Volvo",
                           ano=2025,
                           cor="Verde",
                           valor_fipe=149999)

byd = VeiculoEletrico(placa="JDN0A00",
                              modelo="BYD",
                              marca="BYD",
                              ano=2021,
                              cor="Branco",
                              valor_fipe=950000,
                              nivel_bateria=65)

print(f"{gol.calcular_consumo(distancia):.2f} Litros serão gastos a cada 12 km")
print(f"{cg_125.calcular_consumo(distancia):.2f} Litros serão gastos a cada 20 km")
print(f"{fh.calcular_consumo(distancia):.2f} Litros serão gastos a cada 5 km")
print(f"{byd.calcular_consumo(distancia):.2f} de KWh gasta a cada 0.15 km")

byd.recarregar(100)

frota = Frota(gol)
frota.adicionar_veiculo(cg_125)
frota.adicionar_veiculo(fh)
frota.adicionar_veiculo(byd)

print(f"{frota.consumo_frota(distancia):.2f}")

# Exemplo:
veiculos = [
    Carro(placa="ABC1234", modelo="Gol", marca="Volkswagen", ano=2020, cor="Prata", valor_fipe=50000),
    Moto(placa="XYZ5678", modelo="CG 160", marca="Honda", ano=2021, cor="Preto", valor_fipe=12000),
    VeiculoEletrico(placa="ABC1234", modelo="Leaf", marca="Nissan", ano=2022, cor="Branco", valor_fipe=150000, nivel_bateria=80),
    Caminhao(placa="XYZ5678", modelo="FH", marca="Volvo", ano=2019, cor="Azul", valor_fipe=300000)
]

# Identificando veículos duplicados pela placa
duplicados = []
for i in range(len(veiculos)):
    for j in range(i + 1, len(veiculos)):
        if veiculos[i] == veiculos[j]:
            duplicados.append((veiculos[i], veiculos[j]))

# Exibindo os veículos duplicados
print("\nVeículos duplicados encontrados:")
for v1, v2 in duplicados:
    print(f"Duplicado: {v1} e {v2}")
