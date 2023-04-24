# Elabore uma estrutura para representar um produto (código, nome, preço). Cadastre 5 produtos, use vetor/lista. Aplique 10% de aumento no preço do produto e apresente todos os dados do preço. Não use função.

class classProduto:
    codigo = 0
    nome = ''
    preco = 0.0


arrayProdutos = []

for i in range(5):
    Produto = classProduto()

    Produto.codigo = int(input('Cadastre o código do produto: '))
    Produto.nome = input('Cadastre o nome do produto: ')
    Produto.preco = float(input('Cadastre o preço do produto: '))

    Produto.preco += Produto.preco * 10 / 100

    arrayProdutos.append(Produto)
    
for i in range(5):
    print(f'Código: {arrayProdutos[i].codigo}, Nome: {arrayProdutos[i].nome}, Preço: {arrayProdutos[i].preco}')