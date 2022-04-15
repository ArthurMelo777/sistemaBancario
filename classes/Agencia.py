from classes import Endereco
from classes.conta import Conta


class Agencia:
    def __init__(self, numero, endereco: Endereco):
        self.numero = numero
        self.contas = []
        self.endereco = endereco

    def add_conta(self, *conta: Conta):
        conta_nova = Conta
        if len(conta) < 1:
            nome = input("Informe seu nome: ").capitalize()
            tipo = input("Informe o tipo da conta Poupança/Corrente: ")[0].upper()
            saldo = float(input("Informe o depósito inicial: "))
            saldo = 0 if saldo < 0 else saldo
            conta_nova = Conta(nome, saldo, tipo, self.numero)
            self.contas.append(conta_nova)
            return conta_nova
        else:
            self.contas.append(conta[0])

