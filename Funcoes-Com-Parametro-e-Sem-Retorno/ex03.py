# Faça uma função/método para a partir de um preço de um produto informado, calcular e apresentar o novo preço reajustado em 9%.

def reajuste(preco):
    valor = preco * 0.09
    
    print(f'O novo preço é R$ {preco + valor}')

def main():
    preco = float(input('Insira o preço inicial: '))
    
    reajuste(preco)

main()