import os

from classes import bd, conta


def menu():
    os.system('cls')
    print("BEM VINDO AO SEU APP DE BANCO!")
    print("Escolha a opção desejada abaixo:")
    print("1 - Inserir conta")
    print("2 - Consultar todas as contas")
    print("3 - Consultar uma conta")
    print("4 - Movimentar conta")
    print("5 - Excluir conta")
    print("0 - Finalizar programa")
    opc = int(input())
    os.system('cls')
    return opc


class Menu:
    bd = bd.BD()

    def inserir(self):
        print(
            "Digite, na mesma linha e respectivamente: o NOME, o SALDO, o TIPO DA CONTA, a AGÊNCIA DA CONTA que deseja cadastrar: ")
        c = input().split(' ')
        con = conta.Conta(c[0], c[1], c[2], c[3])
        self.bd.inserirValores(con)
        input("Usuario cadastrado com sucesso! Press qqr tecla para continuar")
        os.system('cls')

    def lerTudo(self):
        r = self.bd.lerValores()
        if len(r) > 0:
            for i in r:
                print(i)
            input("Press qqr tecla para continuar")
        else:
            print("Não há contas cadastradas!")
            input("Press qqr tecla para continuar")
        os.system('cls')

    def lerConta(self):
        identify = input("Digite o número do ID da conta que deseja consultar: ")
        print(self.bd.lerValores(identify))
        input("Press qqr tecla para continuar")
        os.system('cls')

    def atualizarConta(self):
        print("Digite, respectivamente, o valor e o ID da conta que deseja atualizar: ")
        print("OBS: Os valores devem ser negativos para saques e positivos para depósitos")
        v = input().split(' ')

        self.bd.atualizarValores(int(v[0]), v[1])
        input("Valor atualizado com sucesso! Press qqr tecla para continuar")
        os.system('cls')

    def removerConta(self):
        identify = input("Digite o número do ID da conta que deseja remover: ")
        self.bd.excluirValores(identify)
        input("Conta removida com sucesso! Press qqr tecla para continuar")
        os.system('cls')

    def continuar(self):
        print("Deseja continuar e realizar outra operação?")
        print("1 - Sim")
        print("2 - Não")
        opc = int(input())
        os.system('cls')
        if opc == 1:
            opc = int(menu())
        else:
            self.sair()
            opc = 0
        return opc

    def sair(self):
        print("Obrigado por utilizar nosso programa, até a próxima!")
        self.bd.close()
