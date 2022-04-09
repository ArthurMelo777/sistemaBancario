from classes import bd, conta, menu
import os

## CRIAR CONEXÃO E TABELA
db = bd.BD()
db.criarTabela()

## MENU
m = menu.Menu()
opc = m.menu()

while opc != 0:
    if opc == 1:
        m.inserir()
        opc = m.continuar()
    elif opc == 2:
        m.lerTudo()
        opc = m.continuar()
    elif opc == 3:
        m.lerConta()
        opc = m.continuar()
    elif opc == 4:
        m.atualizarConta()
        opc = m.continuar()
    elif opc == 5:
        m.removerConta()
        opc = m.continuar()
    else:
        m.sair()