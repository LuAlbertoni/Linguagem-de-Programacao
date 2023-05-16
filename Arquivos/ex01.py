# Elabore uma estrutura para representar e armazenar 10 fornecedores (código, nome, endereco). Utilize os recursos de arquivo para armazenar estes dados permanentemente. O nome do arquivo deve ser o mesmo da estrutura. Construa um menu com as seguintes opções, cada uma delas deve ter uma função e a main para chamar todas elas.

# Menu de opções:

# Cadastrar fornecedores
# Visualizar todos os dados
# Sair

class classeFornecedores():
    codigo = 0
    nome = ''
    endereco = ''
    
def menu():
    print('\n# Menu de opções #\n1- Cadastrar fornecedores\n2- Visualizar todos os dados\n3- Sair')
    opcao = int(input('\nInsira a opção desejada: '))
    
    return opcao
    
def cadastro():
    arquivo = open('ex01.txt', 'a')
    
    for i in range(10):
        fornecedor = classeFornecedores()
        
        fornecedor.codigo = int(input('\nDigite o código do fornecedor: '))
        fornecedor.nome = input('Digite o nome do fornecedor: ')
        fornecedor.endereco = input('Digite o endereço do fornecedor: ')
        
        arquivo.write(f'{fornecedor.codigo};{fornecedor.nome};{fornecedor.endereco}\n')
        
    arquivo.close()

def visualizar():
    arquivo = open('ex01.txt', 'r')
    
    for fornecedor in arquivo.readlines():
        codigo, nome, endereco = fornecedor.strip().split(';')
        print(f'\nCódigo: {codigo}\nNome: {nome}\nEndereço: {endereco}')
        
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