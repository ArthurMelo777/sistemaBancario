from classes import *

bd = BD()
bd.criarTabela()

conta1 = Conta('Arthur', 500.00, 'C', '0000', '00000-0')
#bd.inserirValores(conta1)
conta1.depositarValor(100.0)
print(conta1.saldo)