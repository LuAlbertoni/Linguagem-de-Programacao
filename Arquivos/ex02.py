# Elabore uma estrutura para representar e armazenar 10 produtos (código, nome, preço). Utilize os recursos de arquivo para armazenar estes dados permanentemente. O nome do arquivo deve ser o mesmo da estrutura. Construa um menu com as seguintes opções, cada uma delas deve ter uma função e a main para chamar todas elas.
# Menu de opções:

# Cadastrar produtos
# Visualizar todos os dados
# Sair

class classeProdutos():
    codigo = 0
    nome = ''
    preco = 0

def menu():
    print('\n# Menu de opções #\n1- Cadastrar produtos\n2- Visualizar todos os dados\n3- Sair')
    opcao = int(input('\nInsira a opção desejada: '))
    
    return opcao

def cadastro():
    arquivo = open('ex02.txt', 'a')
    
    for i in range(10):
        produto = classeProdutos()
    
        produto.codigo = int(input('\nDigite o código do produto: '))
        produto.nome = input('Digite o nome do produto: ')
        produto.preco = float(input('Digite o preço do produto: '))
    
        arquivo.write(f'{produto.codigo};{produto.nome};{produto.preco}\n')

    arquivo.close()
    
def visualizar():
    arquivo = open('ex02.txt', 'r')
    
    for produto in arquivo.readlines():
        codigo, nome, preco = produto.strip().split(';')
        print(f'\nCódigo: {codigo}\nNome: {nome}\nPreço: {preco}')
    
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