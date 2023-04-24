# Uma escola precisa montar o cadastro geral de seus alunos. Este cadastro deverá conter as seguintes informações por aluno: nome completo, data de nascimento, telefone, endereço e série atual. Levando em conta que esta escola possui no máximo 500 alunos, como você faria para estruturar estas informações num sistema de gerenciamento para a escola? Implemente utilizando estrutura. Também use a criação de funções para cada operação. Use o menu a seguir:
# Menu de opções:

# Cadastrar alunos
# Consulta por nome
# Visualizar todos os dados
# Sair

class classAluno:
    nome = ''
    data_nascimento = ''
    telefone = ''
    endereco = ''
    serie_atual = ''


def menu():
    opcao = 0

    while opcao < 1 or opcao > 4:
        print('\nMenu de opções:\n 1. Cadastrar alunos\n 2. Consulta por nome\n 3. Visualizar todos os dados\n 4. Sair')
        opcao = int(input('Qual opção deseja? '))

        if opcao < 1 or opcao > 4:
            print('\nOpção inválida!')

    return opcao


def cadastrar(arrayAlunos):
    aluno = classAluno()

    aluno.nome = input('Cadastre o nome do aluno: ')
    aluno.data_nascimento = input('Cadastre a data de nascimento do aluno: ')
    aluno.telefone = input('Cadastre o telefone do aluno: ')
    aluno.endereco = input('Cadastre o endereço do aluno: ')
    aluno.serie_atual = input('Cadastre a série atual do aluno: ')

    arrayAlunos.append(aluno)

    return arrayAlunos


def consultar(arrayAlunos):
    nome = input('Digite o nome do aluno: ')

    for i in range(len(arrayAlunos)):
        if arrayAlunos[i].nome == nome:
            print(f'Nome: {arrayAlunos[i].nome}\nData de nascimento: {arrayAlunos[i].data_nascimento}\nTelefone: {arrayAlunos[i].telefone}\nEndereço: {arrayAlunos[i].endereco}\nSérie atual: {arrayAlunos[i].serie_atual}')


def visualizar(arrayAlunos):
    for i in range(len(arrayAlunos)):
        print(f'Nome: {arrayAlunos[i].nome}\nData de nascimento: {arrayAlunos[i].data_nascimento}\nTelefone: {arrayAlunos[i].telefone}\nEndereço: {arrayAlunos[i].endereco}\nSérie atual: {arrayAlunos[i].serie_atual}')


def main():
    opcao = menu()
    arrayAlunos = []

    while opcao != 4 and len(arrayAlunos) < 500:
        if opcao == 1:
            arrayAlunos = cadastrar(arrayAlunos)
        elif opcao == 2:
            consultar(arrayAlunos)
        elif opcao == 3:
            visualizar(arrayAlunos)

        opcao = menu()


main()
