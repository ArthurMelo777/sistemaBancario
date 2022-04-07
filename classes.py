import sqlite3

class BD:
    banco = sqlite3.connect('usuarios.db')
    cursor = banco.cursor()

    def criarTabela(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Contas (id integer PRIMARY KEY AUTOINCREMENT, nome VARCHAR(255), saldo FLOAT, tipoConta CHAR, agencia VARCHAR(4), numeroConta VARCHAR(7))")
    
    def deletarTabela(self):
        self.cursor.execute("DROP TABLE IF EXISTS Contas")

    def inserirValores(self, nome, saldo, tipoConta, agencia, numeroConta):
        self.cursor.execute("INSERT INTO Contas VALUES (NULL, '"+nome+"', "+str(saldo)+", '"+tipoConta+"', '"+agencia+"', '"+numeroConta+"')")
        self.banco.commit()

class Conta:
    bd = BD()
    def __init__ (self, nome, saldo, tipoConta, agencia, numeroConta):
        self.nome = nome
        self.saldo = saldo
        self.tipoConta = tipoConta
        self.agencia = agencia
        self.numeroConta = numeroConta
        self.bd.inserirValores(nome, saldo, tipoConta, agencia, numeroConta)
    
    def depositarValor(self, valor):
        self.saldo = self.saldo + valor
    
    def sacarValor(self, valor):
        self.saldo = self.saldo - valor