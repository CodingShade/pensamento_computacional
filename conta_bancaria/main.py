from models.Conta_bancaria import Conta_bancaria

conta = Conta_bancaria("Thomas", 1000, 10000, [])

conta.depositar(100)
conta.exibir_historico()
conta.exibir_saldo()