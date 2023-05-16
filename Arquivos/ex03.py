# Elabore uma estrutura para representar e armazenar 10 alunos (matricula, nome, telefone). Utilize os recursos de arquivo para armazenar estes dados permanentemente. O nome do arquivo deve ser o mesmo da estrutura. Construa um menu com as seguintes opções, cada uma delas deve ter uma função e a main para chamar todas elas.
# Menu de opções:

# Cadastrar alunos
# Visualizar todos os dados
# Sair

class classeAlunos():
    matricula = 0
    nome = ''
    telefone = ''
    
def menu():
    print('\n# Menu de opções #\n1- Cadastrar alunos\n2- Visualizar todos os dados\n3- Sair')
    opcao = int(input('\nInsira a opção desejada: '))
    
    return opcao

def cadastro():
    arquivo = open('ex03.txt', 'a')
    
    for i in range(10):
        aluno = classeAlunos()
    
        aluno.matricula = int(input('\nDigite a matrícula do aluno: '))
        aluno.nome = input('Digite o nome do aluno: ')
        aluno.telefone = input('Digite o telefone do aluno: ')
    
        arquivo.write(f'{aluno.matricula};{aluno.nome};{aluno.telefone}\n')

    arquivo.close()
    
def visualizar():
    arquivo = open('ex03.txt', 'r')
    
    for aluno in arquivo.readlines():
        matricula, nome, telefone = aluno.strip().split(';')
        print(f'\nMatrícula: {matricula}\nNome: {nome}\nTelefone: {telefone}')
    
    arquivo.close()

def main():
    opcao = menu()
    
    while opcao != 3:
        if opcao == 1:
            cadastro()
        elif opcao == 2:
            visualizar()
        else:
            print('Opção inválida, tente novamente!')
        
        opcao = menu()

main()