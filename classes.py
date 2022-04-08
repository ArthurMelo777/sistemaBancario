import sqlite3

class BD:
    banco = sqlite3.connect('usuarios.db')
    cursor = banco.cursor()
    
    def close(self):
        self.banco.close()

    def criarTabela(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Contas (id integer PRIMARY KEY AUTOINCREMENT, nome VARCHAR(255), saldo FLOAT, tipoConta CHAR, agencia VARCHAR(4), numeroConta VARCHAR(7))")
    
    def deletarTabela(self):
        self.cursor.execute("DROP TABLE IF EXISTS Contas")

    def inserirValores(self, conta):
        c = conta
        self.cursor.execute("INSERT INTO Contas VALUES (NULL, '"+c.nome+"', "+str(c.saldo)+", '"+c.tipoConta+"', '"+c.agencia+"', '"+c.numeroConta+"')")
        self.banco.commit()
    
    def lerValores(self, *id):
        if len(id) == 0:
            self.cursor.execute("SELECT * FROM Contas")
            r = self.cursor.fetchall()
        else:
            self.cursor.execute("SELECT * FROM Contas WHERE id = "+id[0]+"")
            r = self.cursor.fetchall()[0]
        return r
    
    def atualizarValores(self, saldo, numeroConta):
        self.cursor.execute("UPDATE Contas SET saldo = "+str(saldo)+" WHERE numeroConta = '"+numeroConta+"'")
        self.banco.commit()

class Conta:
    bd = BD()
    def __init__ (self, nome, saldo, tipoConta, agencia, numeroConta):
        self.nome = nome
        self.saldo = saldo
        self.tipoConta = tipoConta
        self.agencia = agencia
        self.numeroConta = numeroConta
    
    def depositarValor(self, valor):
        self.saldo = self.saldo + valor
        self.bd.atualizarValores(self.saldo, self.numeroConta)
    
    def sacarValor(self, valor):
        self.saldo = self.saldo - valor
        self.bd.atualizarValores(self.saldo, self.numeroConta)