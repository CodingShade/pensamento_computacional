class ContaBancaria:

    def __init__(self, titular, pix, saldo_inicial=0, limite=0):
        self.titular = titular
        self.saldo = saldo_inicial
        self.limite = limite
        self.ativo = False
        self.pix = pix
        self.historico = []

    def __str__(self):
        status = "Ativa" if self.ativo else "Inativa"
        return f"Conta de {self.titular} | Saldo: R${self.saldo:.2f} | Limite: R${self.limite:.2f} | Status: {status}"

    def ativar_conta(self):
        if not self.ativo:
            self.ativo = True
            self.registrar_transacao("Conta ativada")
            print(f"Conta de {self.titular} ativada com sucesso!")
        else:
            print("A conta já está ativa.")

    def desativar_conta(self):
        if self.ativo:
            if self.saldo == 0:
                self.ativo = False
                self.registrar_transacao("Conta desativada")
                print(f"Conta de {self.titular} desativada com sucesso!")
            else:
                print("Não é possível desativar a conta com saldo diferente de zero.")
        else:
            print("A conta já está inativa.")

    def registrar_transacao(self, descricao, valor=0):
        self.historico.append((descricao, valor))

    def depositar(self, valor):
        if self.ativo:
            if valor > 0:
                self.saldo += valor
                self.registrar_transacao("Depósito", valor)
                print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")
            else:
                print("O valor do depósito deve ser positivo.")
        else:
            print("Conta inativa. Operação não permitida.")

    def sacar(self, valor):
        if self.ativo:
            if 0 < valor <= (self.saldo + self.limite):
                self.saldo -= valor
                self.registrar_transacao("Saque", -valor)
                print(f"Saque de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")
            else:
                print("Valor de saque inválido ou limite excedido.")
        else:
            print("Conta inativa. Operação não permitida.")

    def transferencia(self, conta_destino, valor):
        if self.ativo and conta_destino.ativo:
            if 0 < valor <= (self.saldo + self.limite):
                self.saldo -= valor
                conta_destino.saldo += valor
                self.registrar_transacao(f"Transferência para {conta_destino.titular}", -valor)
                conta_destino.registrar_transacao(f"Transferência de {self.titular}", valor)
                print(f"Transferência de R${valor:.2f} para {conta_destino.titular} realizada com sucesso!")
            else:
                print("Valor de transferência inválido ou limite excedido.")
        else:
            print("Conta de origem ou destino inativa. Operação não permitida.")

    def exibir_historico(self):
        print(f"\nHistórico de transações de {self.titular}:")
        for transacao in self.historico:
            descricao, valor = transacao
            if valor == 0:
                print(f"- {descricao}")
            else:
                print(f"- {descricao}: R${abs(valor):.2f} ({'+' if valor > 0 else '-'})")
        print(f"Saldo atual: R${self.saldo:.2f}")