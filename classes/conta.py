class Conta:
    def __init__ (self, nome, saldo, tipoConta, agencia, numeroConta):
        self.nome = nome
        self.saldo = saldo
        self.tipoConta = tipoConta
        self.agencia = agencia
        self.numeroConta = numeroConta
    
    def movimentarValor(self, valor):
        return self.saldo + valor