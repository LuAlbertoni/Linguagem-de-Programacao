# Faça uma função/método para a partir de um preço de um produto informado, calcular e apresentar o novo preço reajustado em alguma porcentagem que deve ser informada pelo usuário e será um parâmetro.

def reajuste(preco, porcentagem):
    valor = preco * (porcentagem / 100)
    
    print(f'O novo preço é R$ {preco + valor}')

def main():
    preco = float(input('Insira um preço: '))
    porcentagem = float(input('Insira a porcentagem do reajuste: '))
    
    reajuste(preco, porcentagem)

main()