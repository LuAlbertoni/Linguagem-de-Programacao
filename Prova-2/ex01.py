# Em Python crie um programa que atenda o menu a seguir. Desenvolva uma função para cada opção do menu. Utilize a criação de estruturas. Cadastrar 5 (vetor) compras e 2 (vetor) clientes.

# CLIENTES	-	COMPRAS
# cod_cli	-	cod_comp
# nome	-	cod_cli
# saldo_cashback	-	valor

# Menu de Opções

# 1 Cadastrar clientes
# 2 Mostrar todos os clientes
# 3 Cadastrar compras
# 4 Mostrar todas as compras
# 5 Mostrar o total de todas as compras realizadas por um cliente
# 6 Armazenar todas as compras em arquivo
# 7 Apresentar o conteúdo do arquivo
# 8 Gerar um gráfico
# 9 Sair

# Observaçôes:

# Na opção 3, o valor da compra, deve ser descontado no saldo do cashback do cliente que a realizou. Por exemplo, cliente 1, tem 500 de saldo, se ele realizar uma compra de 100 reais, o saldo do cashback passará para 400.
# Na opção 5, o usuário do sistema informará/digitará o código do cliente que quer e o sistema/programa fará uma pesquisa e calculará o total de compras do determinado cliente.
# Na opção 6 use a função write antes da estrutura de repetição para armazenar o cabeçalho das colunas, depois dentro do laço grave todos os campos do tipo Compras como foi visto em aula, no arquivo de nome compras.csv. Use como sepador entre colunas/campos a , vírgula
# Na opção 7 apresente todos os dados armazenados no arquivo compras.csv
# Na opção 8 use a coluna valor no gráfico e adote a cor orange da biblioteca Matplotlib

import pandas as pd
import matplotlib.pyplot as plt


class Clientes:
    cod_cli = 0
    nome = ''
    saldo_cashback = 0


class Compras:
    cod_cli = 0
    cod_comp = 0
    valor = 0

# Menu de Opções


def menu():
    opcao = 0

    while opcao < 1 or opcao > 9:
        print('\nMenu de opções\n1- Cadastrar clientes\n2- Mostrar todos os clientes\n3- Cadastrar compras\n4- Mostrar todas as compras\n5- Mostrar o total de todas as compras realizadas por um cliente\n6- Armazenar todas as compras em arquivo\n7- Apresentar o conteúdo do arquivo\n8- Gerar um gráfico\n9- Sair\n')

        opcao = int(input('Digite a opção desejada: '))

        if opcao < 1 or opcao > 9:
            print('Opção inválida!')

    return opcao

# Cadastro


def cadastroClientes(arrayClientes):
    cliente = Clientes()
    codigo = -1

    while codigo == -1:
        codigo = int(input('\nDigite o código do cliente: '))

        for i in range(len(arrayClientes)):
            if codigo == arrayClientes[i].cod_cli:
                codigo = -1
                print('Código já cadastrado!')

    cliente.cod_cli = codigo
    cliente.nome = input('Digite o nome do cliente: ')
    cliente.saldo_cashback = float(input('Digite o saldo do cashback: '))

    arrayClientes.append(cliente)

    return arrayClientes


def cadastroCompras(arrayCompras, arrayClientes):
    compra = Compras()
    codigoProduto = -1
    pos = -1

    while pos == -1:
        codigoCliente = int(input('\nDigite o código do cliente: '))

        for i in range(len(arrayClientes)):
            if codigoCliente == arrayClientes[i].cod_cli:
                pos = i
                break

        if pos == -1:
            print('Código não cadastrado!')

    while codigoProduto == -1:
        codigoProduto = int(input('Digite o código do produto: '))

        for i in range(len(arrayCompras)):
            if codigoProduto == arrayCompras[i].cod_cli:
                codigoProduto = -1
                print('Código já cadastrado!')

    compra.cod_cli = codigoCliente
    compra.cod_comp = codigoProduto
    compra.valor = float(input('Digite o valor da compra: '))

    arrayCompras.append(compra)

    if arrayClientes[pos].saldo_cashback > 0:
        if arrayClientes[pos].saldo_cashback >= compra.valor:
            arrayClientes[pos].saldo_cashback -= compra.valor
        else:
            arrayClientes[pos].saldo_cashback = 0

    return arrayCompras, arrayClientes

# Exibição


def mostrarClientes(arrayClientes):
    print('\nClientes cadastrados:')
    for i in range(len(arrayClientes)):
        print(
            f'\nCódigo: {arrayClientes[i].cod_cli}\nNome: {arrayClientes[i].nome}\nSaldo: {arrayClientes[i].saldo_cashback}')


def mostrarCompras(arrayCompras):
    print('\nCompras cadastradas:')
    for i in range(len(arrayCompras)):
        print(
            f'\nCódigo: {arrayCompras[i].cod_comp}\nCódigo do cliente: {arrayCompras[i].cod_cli}\nValor: {arrayCompras[i].valor}')


def mostrarTotalCompras(arrayCompras, arrayClientes):
    codigo = -1
    total = 0
    pos = -1

    while pos == -1:
        codigo = int(input('\nDigite o código do cliente: '))

        for i in range(len(arrayClientes)):
            if codigo == arrayClientes[i].cod_cli:
                pos = i
                break

        if pos == -1:
            print('Código não cadastrado!')

    for i in range(len(arrayCompras)):
        if codigo == arrayCompras[i].cod_cli:
            total += arrayCompras[i].valor

    print(f'\nTotal das compras: {total}')

# Arquivo


def armazenarCompras(arrayCompras):
    arquivo = open('compras.csv', 'w')

    arquivo.write('cod_cli,cod_comp,valor\n')

    for i in range(len(arrayCompras)):
        arquivo.write(
            f'{arrayCompras[i].cod_cli},{arrayCompras[i].cod_comp},{arrayCompras[i].valor}\n')

    arquivo.close()

    print('\nArquivo gerado com sucesso!')


def apresentarArquivo():
    arquivo = open('compras.csv', 'r')

    for i in arquivo.readlines():
        cod_cli, cod_comp, valor = i.strip().split(",")
        print(cod_cli, '\t', cod_comp, '\t', valor)

    arquivo.close()

# Gráfico


def gerarGrafico():
    df = pd.read_csv('compras.csv')

    qnt = len(df)

    plt.bar(range(qnt), df['valor'], color='orange')
    plt.ylabel('Valor gasto')
    plt.title('Valor gasto por compra')
    plt.show()


def main():
    arrayClientes = []
    arrayCompras = []

    opcao = menu()

    while opcao != 9:
        if opcao == 1:
            if len(arrayClientes) < 2:
                cadastroClientes(arrayClientes)
            else:
                print('\nNúmero máximo de clientes cadastrados!')
        elif opcao == 2:
            mostrarClientes(arrayClientes)
        elif opcao == 3:
            if len(arrayClientes) < 5:
                cadastroCompras(arrayCompras, arrayClientes)
            else:
                print('\nNúmero máximo de compras cadastradas!')
        elif opcao == 4:
            mostrarCompras(arrayCompras)
        elif opcao == 5:
            mostrarTotalCompras(arrayCompras, arrayClientes)
        elif opcao == 6:
            armazenarCompras(arrayCompras)
        elif opcao == 7:
            apresentarArquivo()
        elif opcao == 8:
            gerarGrafico()
        elif opcao == 9:
            break

        opcao = menu()


main()
