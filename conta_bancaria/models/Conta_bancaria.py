1
# Lista global para armazenar contas bancárias
contas = []

def criar_conta():
    print("\n--- Criar Nova Conta ---")
    titular = input("Nome do titular: ")
    saldo = float(input("Saldo inicial: R$ "))
    limite = float(input("Limite de crédito: R$ "))
    nova_conta = (titular, saldo, limite, [])
    contas.append(nova_conta)
    print(f"Conta criada com sucesso para {titular}!")

def encontrar_conta(titular):
    for conta in contas:
        if conta.titular.lower() == titular.lower():
            return conta
    return None

def exibir_saldo():
    print("\n--- Exibir Saldo ---")
    titular = input("Nome do titular da conta: ")
    conta = encontrar_conta(titular)
    if conta:
        print(f"Saldo atual de {conta.titular}: R$ {conta.saldo:.2f}")
    else:
        print("Conta não encontrada!")

def sacar():
    print("\n--- Sacar ---")
    titular = input("Nome do titular da conta: ")
    conta = encontrar_conta(titular)
    if conta:
        valor = float(input("Valor a sacar: R$ "))
        conta.sacar(valor)
    else:
        print("Conta não encontrada!")

def depositar():
    print("\n--- Depositar ---")
    titular = input("Nome do titular da conta: ")
    conta = encontrar_conta(titular)
    if conta:
        valor = float(input("Valor a depositar: R$ "))
        conta.depositar(valor)
    else:
        print("Conta não encontrada!")

def transferir():
    print("\n--- Transferir ---")
    remetente = input("Nome do titular da conta de origem: ")
    conta_remetente = encontrar_conta(remetente)
    if not conta_remetente:
        print("Conta de origem não encontrada!")
        return

    destinatario = input("Nome do titular da conta de destino: ")
    conta_destinatario = encontrar_conta(destinatario)
    if not conta_destinatario:
        print("Conta de destino não encontrada!")
        return

    valor = float(input("Valor a transferir: R$ "))
    conta_remetente.transferencia(conta_destinatario, valor)

def exibir_historico():
    print("\n--- Histórico de Transações ---")
    titular = input("Nome do titular da conta: ")
    conta = encontrar_conta(titular)
    if conta:
        conta.exibir_historico()
    else:
        print("Conta não encontrada!")

def excluir_conta():
    print("\n--- Excluir Conta ---")
    titular = input("Nome do titular da conta a ser excluída: ")
    conta = encontrar_conta(titular)
    if not conta:
        print("Conta não encontrada!")
        return

    # Verificar saldo
    if conta.saldo > 0:
        print(f"Saldo restante: R$ {conta.saldo:.2f}")
        opcao = input("Deseja transferir o saldo para outra conta? (s/n): ").lower()
        if opcao == 's':
            destinatario = input("Nome do titular da conta de destino: ")
            conta_destino = encontrar_conta(destinatario)
            if conta_destino:
                conta.transferencia(conta_destino, conta.saldo)
            else:
                print("Conta de destino não encontrada!")
                return
    elif conta.saldo < 0:
        print(f"Saldo negativo: R$ {conta.saldo:.2f}")
        opcao = input("Deseja depositar para zerar a conta? (s/n): ").lower()
        if opcao == 's':
            valor = abs(conta.saldo)
            conta.depositar(valor)
        else:
            print("Não é possível excluir a conta com saldo negativo.")
            return

    # Remover a conta da lista
    contas.remove(conta)
    print(f"Conta de {conta.titular} excluída com sucesso!")

def menu():
    while True:
        print("\n=== Menu Bancário ===")
        print("1: Criar conta")
        print("2: Exibir saldo")
        print("3: Sacar")
        print("4: Depositar")
        print("5: Realizar transferência")
        print("6: Exibir histórico de transações")
        print("7: Excluir conta")
        print("0: Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_conta()
        elif opcao == "2":
            exibir_saldo()
        elif opcao == "3":
            sacar()
        elif opcao == "4":
            depositar()
        elif opcao == "5":
            transferir()
        elif opcao == "6":
            exibir_historico()
        elif opcao == "7":
            excluir_conta()
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()