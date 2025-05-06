class Conta_bancaria:
    def __init__(self, titular, saldo, limite, historico):
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.historico = historico

    def depositar(self, valor):
        if (valor > 0 ):
            self.saldo += valor
        else:
            print(f"O valor {valor} é invalido!")


    def sacar(self, valor):
        if (valor <= self.saldo):
            self.saldo -= valor
            self.historico.append({})
            print("Saque realizado!")
        else:
            a = input(f"Deseja utilizar o limite? (R$ {self.limite}) [s,n]")
            if (a == "s"):
                if(self.saldo + self.limite) >= valor:
                    self.saldo -= valor
                    print("Saque realizado!")
                else:
                    print("Saldo e limite insuficientes!")
            else:
                print("Operação com limite cancelada!")
    def transferir(self):

    def exibir_saldo(self):
        print(f"O seu saldo é R${self.saldo:.2f}")

    def exibir_historico(self):
        print(f"Historico{self.historico}")