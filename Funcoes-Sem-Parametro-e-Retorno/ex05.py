# Faça uma função/método que receba o preço antigo e atual de um produto, determine o percentual de acréscimo entre esses valores e apresente-o.

def product():
    oldPrice = float(input('Insira o antigo preço do produto: '))
    newPrice = float(input('Insira o novo preço do produto: '))
    
    print(f'O valor aumentou em {((newPrice * 100) / oldPrice) - 100:.2f}%')

def main():
    product()
    
main()