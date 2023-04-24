# Elabore uma estrutura para representar um produto (código, nome, preço). Crie uma função para cadastrar 5 produtos. Crie outra função para aplicar 10% de aumento no preço do produto e apresente, por meio de outra função, todos os dados do produtos cadastrados, após o aumento. Construa uma função para cada opção do menu a seguir:
# Menu do Sistema

# Cadastrar
# Reajustar
# Visualizar
# Sair
# Qual opção deseja?

class TipoProduto:
    codigo = 0
    nome = ''
    preco = 0.0


def menu():
    print('\nMenu do Sistema')
    print('1. Cadastrar')
    print('2. Reajustar')
    print('3. Visualizar')
    print('4. Sair')
    opcao = int(input('Qual opção deseja? '))
    return opcao


def cadastrar(vet_produto):
    for i in range(3):
        p = TipoProduto()
        p.codigo = int(input('Cadastre o código do produto: '))
        p.nome = input('Cadastre o nome do produto: ')
        p.preco = float(input('Cadastre o preço do produto: '))
        vet_produto.append(p)
    return vet_produto


def visualizar(vet_produto):
    for i in range(len(vet_produto)):
        print('Código:', vet_produto[i].codigo, ' Nome:',
              vet_produto[i].nome, ' Preço:', vet_produto[i].preco)


def reajustar(vet_produto):
    for i in range(len(vet_produto)):
        vet_produto[i].preco += vet_produto[i].preco * 10 / 100
    print('Reajuste realizado com sucesso!')
    return vet_produto


def main():
    op = menu()
    v_produto = []
    while op >= 1 and op <= 3:
        if op == 1:
            v_produto = cadastrar(v_produto)
        elif op == 2:
            v_produto = reajustar(v_produto)
        elif op == 3:
            visualizar(v_produto)
        op = menu()


main()
