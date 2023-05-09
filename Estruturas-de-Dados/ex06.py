# Elabore uma estrutura para representar um Funcionario (código, nome, endereço, salário). Para o membro endereço deve-se criar outra estrutura Endereço (logradouro, número, bairro, cidade). Utilize aninhamento de estruturas para resolver este desenvolvimento. Construa uma função para cada opçao do menu a seguir:
# Menu de opções:

# Cadastrar funcionários
# Visualizar todos os dados
# Sair

class classEndereco:
    logradouro = ''
    numero = 0
    bairro = ''
    cidade = ''


class classFuncionario:
    codigo = 0
    nome = ''
    endereco = classEndereco()
    salario = 0


def menu():
    opcao = 0

    while opcao < 1 or opcao > 3:
        print('\nMenu de opções:\n 1. Cadastrar funcionários\n 2. Visualizar todos os dados\n 3. Sair')
        opcao = int(input('Digite a opção desejada: '))

        if opcao < 1 or opcao > 3:
            print('\nOpção inválida!')

    return opcao


def cadastrar(arrayFuncionarios):
    funcionario = classFuncionario()
    funcionario.endereco = classEndereco()
    numero = 0

    while numero == 0:
        numero = int(input('\nDigite o código do funcionário: '))
        for i in range(len(arrayFuncionarios)):
            if arrayFuncionarios[i].codigo == numero:
                print('\nCódigo de funcionário já cadastrado!')
                numero = 0

    funcionario.codigo = numero
    funcionario.nome = input('Digite o nome do funcionário: ')
    funcionario.endereco.logradouro = input(
        'Digite o logradouro do funcionário: ')
    funcionario.endereco.numero = int(
        input('Digite o número da residência do funcionário: '))
    funcionario.endereco.bairro = input('Digite o bairro do funcionário: ')
    funcionario.endereco.cidade = input('Digite a cidade do funcionário: ')
    funcionario.salario = float(input('Digite o salário do funcionário: '))

    arrayFuncionarios.append(funcionario)

    return arrayFuncionarios


def visualizar(arrayFuncionarios):
    for funcionario in arrayFuncionarios:
        print(f'\nFuncionário: {funcionario.nome}\n Código: {funcionario.codigo}\n Endereço: {funcionario.endereco.logradouro}, {funcionario.endereco.numero}, {funcionario.endereco.bairro}, {funcionario.endereco.cidade}\n Salário: {funcionario.salario}')


def main():
    opcao = menu()
    arrayFuncionarios = []

    while opcao != 3:
        if opcao == 1:
            cadastrar(arrayFuncionarios)
        elif opcao == 2:
            visualizar(arrayFuncionarios)

        opcao = menu()


main()
