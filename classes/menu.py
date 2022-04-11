from classes import bd, conta
import os

class Menu:
    bd = bd.BD()
    def menu(self):
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
    
    def inserir(self):
        print("Digite, na mesma linha e respectivamente: o NOME, o SALDO, o TIPO DA CONTA, a AGÊNCIA e o NÚMERO DA CONTA que deseja cadastrar: ")
        c = input().split(' ')
        con = conta.Conta(c[0], c[1], c[2], c[3], c[4])
        self.bd.inserirValores(con)
        press = input("Usuario cadastrado com sucesso! Press qqr tecla para continuar")
        os.system('cls')
    
    def lerTudo(self):
        r = self.bd.lerValores()
        if len(r) > 0:
            for i in r:
                print(i)
            press = input("Press qqr tecla para continuar")
        else:
            print("Não há contas cadastradas!")
            press = input("Press qqr tecla para continuar")
        os.system('cls')
    
    def lerConta(self):
        id = input("Digite o número do ID da conta que deseja consultar: ")
        print(self.bd.lerValores(id))
        press = input("Press qqr tecla para continuar")
        os.system('cls')
    
    def atualizarConta(self):
        print("Digite, respectivamente, o valor e o ID da conta que deseja atualizar: ")
        print("OBS: Os valores devem ser negativos para saques e positivos para depósitos")
        v = input().split(' ')
        
        self.bd.atualizarValores(int(v[0]), v[1])
        press = input("Valor atualizado com sucesso! Press qqr tecla para continuar")
        os.system('cls')
    
    def removerConta(self):
        id = input("Digite o número do ID da conta que deseja remover: ")
        self.bd.excluirValores(id)
        press = input("Conta removida com sucesso! Press qqr tecla para continuar")
        os.system('cls')

    def continuar(self):
        print("Deseja continuar e realizar outra operação?")
        print("1 - Sim")
        print("2 - Não")
        opc = int(input())
        os.system('cls')
        if opc == 1:
            opc = int(self.menu())
        else:
            self.sair()
            opc = 0
        return opc
    
    def sair(self):
        self.bd.close()