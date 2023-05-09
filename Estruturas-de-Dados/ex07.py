# Elabore uma estrutura para representar um Produto (código, nome, data_fabricacao, data_validade, preço). Para o membro data_fabricacao e data_validade, deve-se criar outra estrutura Data (dia, mês, ano). Utilize aninhamento de estruturas para resolver este desenvolvimento. Construa uma função para cada opçao do menu a seguir:
# Menu de opções:

# Cadastrar produtos
# Visualizar todos os dados
# Sair

class classData:
    dia = 0
    mes = 0
    ano = 0


class classProduto:
    codigo = 0
    nome = ''
    data_fabricacao = classData()
    data_validade = classData()
    preco = 0


def menu():
    opcao = 0

    while opcao < 1 or opcao > 3:
        print('\nMenu de opções:\n 1. Cadastrar produtos\n 2. Visualizar todos os dados\n 3. Sair')
        opcao = int(input('Digite a opção desejada: '))

        if opcao < 1 or opcao > 3:
            print('\nOpção inválida!')

    return opcao


def cadastrar(arrayProdutos):
    produto = classProduto()
    produto.data_fabricacao = classData()
    produto.data_validade = classData()
    numero = 0

    while numero == 0:
        numero = int(input('\nDigite o código do produto: '))
        
        for i in range(len(arrayProdutos)):
            if arrayProdutos[i].codigo == numero:
                print('\Código de produto já cadastrado!')
                numero = 0

    produto.codigo = numero
    
    produto.nome = input('Digite o nome do produto: ')
    produto.data_fabricacao.dia = int(
        input('Digite o dia da fabricação do produto: '))
    produto.data_fabricacao.mes = int(
        input('Digite o mês da fabricação do produto: '))
    produto.data_fabricacao.ano = int(
        input('Digite o ano da fabricação do produto: '))
    produto.data_validade.dia = int(
        input('Digite o dia da validade do produto: '))
    produto.data_validade.mes = int(
        input('Digite o mês da validade do produto: '))
    produto.data_validade.ano = int(
        input('Digite o ano da validade do produto: '))
    produto.preco = float(input('Digite o preço do produto: '))
    
    arrayProdutos.append(produto)

    return arrayProdutos

def visualizar(arrayProdutos):
    for i in range(len(arrayProdutos)):
        print(f'\nCódigo: {arrayProdutos[i].codigo}\nNome: {arrayProdutos[i].nome}\nData de fabricação: {arrayProdutos[i].data_fabricacao.dia}/{arrayProdutos[i].data_fabricacao.mes}/{arrayProdutos[i].data_fabricacao.ano}\nData de validade: {arrayProdutos[i].data_validade.dia}/{arrayProdutos[i].data_validade.mes}/{arrayProdutos[i].data_validade.ano}\nPreço: {arrayProdutos[i].preco}')

def main():
    opcao = menu()
    arrayProdutos = []

    while opcao != 3:
        if opcao == 1:
            cadastrar(arrayProdutos)
        elif opcao == 2:
            visualizar(arrayProdutos)

        opcao = menu()


main()
