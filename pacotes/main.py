from pacotes.interface.interface import *
from pacotes.arquivo.arquivo import *
from time import sleep


def main():
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
            nome = ""

            while nome == "":
                nome = input("Nome: ").strip()

                if nome == "":
                    print("Nome não pode ser vazio")


            idade = leiaInt(input("Idade: "))

            cadastrar(arq,nome,idade)

        elif resposta == 3:
            cabecalho('Saindo do Sistema...')
            break
        else:
            print('Digite uma opção válida!')
        sleep(2)

if __name__ == "__main__":
    main()