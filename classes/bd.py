import sqlite3, os
from classes import conta


class BD:
    banco = sqlite3.connect('usuarios.db')
    cursor = banco.cursor()

    def close(self):
        self.banco.close()

    def criarTabela(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS Contas (id integer PRIMARY KEY AUTOINCREMENT, nome VARCHAR(255), saldo FLOAT, tipoConta CHAR, agencia VARCHAR(4), numeroConta VARCHAR(7))")

    def criarTableAgencia(self):
        self.cursor.execute(
            f"CREATE TABLE IF NOT EXISTS Agencia (id integer PRIMARY KEY AUTOINCREMENT, numero VARCHAR(15), endereco VARCHAR(255))")

    def deletarTabela(self):
        self.cursor.execute("DROP TABLE IF EXISTS Contas")

    def inserirValores(self, conta):
        c = conta

        ## VERIFICAÇÃO
        while c.verificarNome():  ## verificar nome
            c.nome = input("Nome inválido. Por favor insira um nome entre 1 e 255 caracteres: ")
            os.system('cls')

        if c.verificarTipoConta():  ## verificar tipo da conta
            while c.verificarTipoConta():
                c.tipoConta = input("Tipo de conta inválido. Por informe se a conta é corrente ou poupança: ")
                os.system('cls')
        else:
            c.tipoConta = c.tipoConta.upper()
            if c.tipoConta == 'POUPANÇA' or c.tipoConta == 'POUPANCA' or c.tipoConta == 'P':
                c.tipoConta = 'P'
            if c.tipoConta == 'CORRENTE' or c.tipoConta == 'C':
                c.tipoConta = 'C'

        while c.verificarAgencia():  ## verificar agencia
            c.agencia = input("Agência inválida. Por favor insira uma agência válida (ex: 0000): ")
            os.system('cls')

        self.cursor.execute("INSERT INTO Contas VALUES (NULL, '" + c.nome + "', " + str(
            c.saldo) + ", '" + c.tipoConta + "', '" + c.agencia + "', '" + c.numeroConta + "')")
        self.banco.commit()

    def lerValores(self, *id):
        if len(id) == 0:
            self.cursor.execute("SELECT * FROM Contas")
            r = self.cursor.fetchall()
        else:
            self.cursor.execute("SELECT * FROM Contas WHERE id = " + str(id[0]) + "")
            r = self.cursor.fetchall()[0]
        return r

    def atualizarValores(self, valor, id):
        v = self.lerValores(id)
        c = conta.Conta(v[1], v[2], v[3], v[4], v[5])
        saldo = c.movimentarValor(valor)
        self.cursor.execute("UPDATE Contas SET saldo = " + str(saldo) + " WHERE id = " + id + "")
        self.banco.commit()

    def excluirValores(self, id):
        self.cursor.execute("DELETE FROM Contas WHERE id = " + id + "")
        self.banco.commit()
