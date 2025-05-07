from models.Conta_bancaria import Conta_bancaria

conta = Conta_bancaria("Thomas", 1000, 500, [])
conta2 = Conta_bancaria("Marcos", 1000, 500, [])

conta.depositar(150)
conta.exibir_historico()
conta.sacar(100)
conta.exibir_historico()
