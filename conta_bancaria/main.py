from models.Conta_bancaria import Conta_bancaria

banco = []

banco.append(Conta_bancaria("Thomas", 1000, 500, []))
banco.append(Conta_bancaria("Pedro", 1000, 500, []))
banco.append(Conta_bancaria("João", 1000, 500, []))

while True:
    print("Menu de opções:")
    menu = input("1 - Criar conta" \
    "2 - Exibir saldo" \
    "3 - Sacar" \
    "4 - Depositar" \
    "5 - Realizar transferencia" \
    "6 - Exibir Historico de transação" \
    "7 - Excluir conta" \
    "8 - Sair")
    if (menu == 1):
        nome = ("Digite seu nome: ")
        saldo = ("Digite seu saldo atual: ")
        if (saldo < 0):
            print("Valor invalido!")
        else:
            banco.append(Conta_bancaria(nome, saldo, 500, []))
    else:
        break        
    



titular = input("Digite o nome da conta que você quer ver:")
for conta in banco:
    if conta.titular == titular:
        print(f"O {titular} tem R$ {conta.saldo} em conta")

