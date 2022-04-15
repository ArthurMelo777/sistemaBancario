class Conta:
    numeral: int = 9999
    digit: int = 0

    def __init__(self, nome, saldo, tipoConta, agencia):
        Conta.digit = (Conta.digit + 1) % 10
        Conta.numeral = Conta.numeral + 1
        self.numeroConta: str = f'{self.numeral} - {self.digit}'
        self.nome = nome
        self.saldo = saldo
        self.tipoConta = tipoConta
        self.agencia = agencia

    def movimentarValor(self, valor):
        return self.saldo + valor

    def verificarNome(self):
        if len(self.nome) > 255 or len(self.nome) == 0:
            return True
        else:
            return False

    def verificarTipoConta(self):
        string = self.tipoConta.upper()
        if string == 'POUPANÇA' or string == 'POUPANCA' or string == 'CORRENTE' or string == 'C' or string == 'P':
            return False
        else:
            return True

    def verificarAgencia(self):
        if len(self.agencia) == 4:
            return False
        else:
            return True

    def verificarNumeroConta(self):
        if len(self.numeroConta) == 7 and self.numeroConta[5] == "-":
            return False
        else:
            return True
