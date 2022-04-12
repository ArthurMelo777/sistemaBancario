class Conta:
    def __init__ (self, nome, saldo, tipoConta, agencia, numeroConta):
        self.nome = nome
        self.saldo = saldo
        self.tipoConta = tipoConta
        self.agencia = agencia
        self.numeroConta = numeroConta
    
    def movimentarValor(self, valor):
        return self.saldo + valor
    
    def verificarNome(self):
        if len(self.nome) > 255 or len(self.nome) == 0:
            return True
        else: return False
    
    def verificarTipoConta(self):
        string = self.tipoConta.upper()
        if string == 'POUPANÇA' or string == 'POUPANCA' or string == 'CORRENTE' or string == 'C' or string == 'P':
            return False
        else:
            return True
    
    def verificarAgencia(self):
        if len(self.agencia) == 4:
            return False
        else: return True
    
    def verificarNumeroConta(self):
        if len(self.numeroConta) == 7 and self.numeroConta[5] == "-":
            return False
        else: return True