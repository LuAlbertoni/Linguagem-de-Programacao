# Faça um programa que realize o cadastro de contas bancarias com as seguintes informações: numero da conta, nome do titular e saldo. O banco permitirá o cadastramento de 15 contas. Crie uma função para cada opção do menu a seguir. Utilize a estrutura na passagem de parâmetro:
# Menu de opções:

# Cadastrar contas
# Visualizar todas as contas
# Consultar por nome
# Alterar nome e/ou saldo de um número de conta
# Excluir a conta com menor saldo
# Sair

# Observação:
# No item de menu 4. Alterar nome e/ou saldo de um número de conta, entenda que apenas pode ser alterado o nome e o saldo depois que você pesquisar pelo número da conta.
# No item 5 do menu, encontre o menor saldo dentre todos cadastrados, depois exclua esta ÚNICA conta.. O assunto de excluir algo de um vetor foi dado na disciplina de Algoritmo.

class classConta:
    numero = 0
    nome = ''
    saldo = 0


def menu():
    opcao = 0

    while opcao < 1 or opcao > 6:
        print('\nMenu de opções:\n 1. Cadastrar contas\n 2. Visualizar todas as contas\n 3. Consultar por nome\n 4. Alterar nome e/ou saldo de um número de conta\n 5. Excluir a conta com menor saldo\n 6. Sair')
        opcao = int(input('Qual opção deseja? '))

        if opcao < 1 or opcao > 6:
            print('\nOpção inválida!')

    return opcao


def cadastrar(arrayContas):
    conta = classConta()

    numero = 0

    while numero == 0:
        numero = int(input('\nCadastre o número da conta: '))

        for i in range(len(arrayContas)):
            if arrayContas[i].numero == numero:
                print('\nNúmero de conta já cadastrado!')
                numero = 0

    conta.numero = numero

    conta.nome = input('Cadastre o nome do titular: ')
    conta.saldo = float(input('Cadastre o saldo: '))

    arrayContas.append(conta)

    return arrayContas


def visualizar(arrayContas):
    for i in range(len(arrayContas)):
        print(
            f'\nNúmero da conta: {arrayContas[i].numero}\nNome do titular: {arrayContas[i].nome}\nSaldo: {arrayContas[i].saldo}')


def consultar(arrayContas):
    nome = input('Digite o nome do titular: ')

    for i in range(len(arrayContas)):
        if arrayContas[i].nome == nome:
            print(
                f'\nNúmero da conta: {arrayContas[i].numero}\nNome do titular: {arrayContas[i].nome}\nSaldo: {arrayContas[i].saldo}')


def alterar(arrayContas):
    numero = int(input('Digite o número da conta: '))
    localizado = -1

    for i in range(len(arrayContas)):
        if arrayContas[i].numero == numero:
            localizado = i

    if localizado != -1:
        opcao = input('Deseja alterar o nome? (S/N) ')

        if opcao == 'S':
            arrayContas[localizado].nome = input('Digite o novo nome: ')

        opcao = input('Deseja alterar o saldo? (S/N) ')

        if opcao == 'S':
            arrayContas[localizado].saldo = float(
                input('Digite o novo saldo: '))

    else:
        print('Conta não localizada!')

    return arrayContas


def excluir(arrayContas):
    menor = 0

    for i in range(len(arrayContas)):
        if arrayContas[i].saldo < arrayContas[menor].saldo:
            menor = i

    print(
        f'\nConta excluída: {arrayContas[menor].numero} - {arrayContas[menor].nome} - {arrayContas[menor].saldo}')
    arrayContas.pop(menor)

    return arrayContas


def main():
    opcao = menu()
    arrayContas = []

    while opcao != 6 and len(arrayContas) < 15:
        if opcao == 1:
            arrayContas = cadastrar(arrayContas)
        elif opcao == 2:
            visualizar(arrayContas)
        elif opcao == 3:
            consultar(arrayContas)
        elif opcao == 4:
            alterar(arrayContas)
        elif opcao == 5:
            excluir(arrayContas)

        opcao = menu()


main()
