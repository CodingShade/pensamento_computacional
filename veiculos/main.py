from models.Veiculos import Veiculos
from models.CarrosCombustao import CarrosCombustao

voyage = Veiculos("BCE9D36", "Voyage", "Volkswagen", "Vermelho", 2018, 47793)
jetta_gli = CarrosCombustao("JDM9DM6", "Jetta GLI", "Volkswagen", "Amarelo", 2025, 150000, "gasolina", 4, 5, 2000, "AT 7" )

print(voyage)
print(jetta_gli)