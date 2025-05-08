import time


class Conta_bancaria:

    '''
    Classe que implementa métodos para manipular uma conta bancaria.add()
    Atributos: titular (str), saldo(float), limite(float) e historicos (lista de dicionarios)

    OBS: Operações no histórico: 0 - sacar, 1 - depositar, 2 - tranferir
    '''

    def __init__(self, titular, saldo, limite, historico):

        """
        Construtor da classe Conta_bancaria
        """

        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.historico = historico

    def depositar(self, valor, remetente = None):
        """
        Metodo que realiza o deposito na conta bancaria.
        Entrada: valor(float)
        Return: True se a operação foi realizada com sucesso
                False se a operação não foi realizada
        """
        op = 1
        if (remetente != None):
            op = 2
        if (valor > 0 ):
            self.saldo += valor
            self.historico.append({"op": op,
                                   "remetente": remetente,
                                   "destinatario": self.titular,
                                   "valor": valor,
                                   "saldo": self.saldo,
                                   "dataetempo": int(time.time())})
            print("Deposito realizado!")
            return True
        else:
            print(f"O valor {valor} é invalido!")
            return False


    def sacar(self, valor, destinatario = None):
        op = 0
        if (destinatario != None):
            op = 2
        if (valor <= self.saldo):
            self.saldo -= valor
            self.historico.append({"op": op,
                                   "remetente": self.titular,
                                   "destinatario": destinatario,
                                   "valor": valor,
                                   "saldo": self.saldo,
                                   "dataetempo": int(time.time())})
            print("Saque realizado!")
            return True
        else:
            a = input(f"Deseja utilizar o limite? (R$ {self.limite}) [s,n]")
            if (a == "s"):
                if(self.saldo + self.limite) >= valor:
                    self.saldo -= valor
                    print("Saque realizado!")
                    return True
                else:
                    print("Saldo e limite insuficientes!")
            else:
                print("Operação com limite cancelada!")
        return False
    
    def transferencia(self, destinatario, valor):
        '''
        Objetivo: método para transferir um valor entre duas contas.
        Entradas: valor(float) e obj Conta_bancaria do destinatário.
        Saída: Se ok -> True, Se NOK -> False.
        '''
        # se o saque ocorrer com sucesso
        if self.sacar(valor, destinatario.titular): #valor = o que quero mudar e destinatario.titular = pra quem quero mandar
            # deposita na conta do destinatario
            destinatario.depositar(valor, self.titular)
            



    def exibir_historico(self):
        print(f"Histórico de transações:")
        for transacao in self.historico:
            dt = time.localtime(transacao["dataetempo"])
            print("Op: ", transacao["op"],
                    "Remetente: ", transacao["remetente"],
                    "Destinatario: ", transacao["destinatario"],
                    "Saldo: ",  transacao["saldo"],
                    "Valor: ", transacao["valor"],
                    "Data e tempo: ",
                    str(dt.tm_hour) + ":" + str(dt.tm_min) + ":" + str(dt.tm_sec) , str(dt.tm_mday) + "/" + str(dt.tm_mon) + "/" + str(dt.tm_year))

    

