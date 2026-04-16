from pacotes.interface.interface import *
from pacotes.arquivo.arquivo import *
from time import sleep

arq = 'Cadastro.txt'
if not arquivoExiste(arq):
   criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #Opção de visualizar as pessoas cadastradas na lista
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = input('Nome: ')
        idade = leiaInt('Idade: ')
        cadastrar(arq,nome,idade)
    elif resposta == 3:
        cabecalho('Saindo do Sistema...')
        break
    else:
        print('Digite uma opção válida!')
    sleep(2)