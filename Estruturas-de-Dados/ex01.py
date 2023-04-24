# Elabore uma estrutura para representar um produto (código, nome, preço). Aplique 10% de aumento no preço do produto e apresente. Não use função.

class classProduto:
    codigo = 0
    nome = ''
    preco = 0.0


Produto = classProduto()

Produto.codigo = int(input('Cadastre o código do produto: '))
Produto.nome = input('Cadastre o nome do produto: ')
Produto.preco = float(input('Cadastre o preço do produto: '))

Produto.preco += Produto.preco * 10 / 100

print(f'Código: {Produto.codigo}, Nome: {Produto.nome}, Preço: {Produto.preco}')
