# Faça uma função/método sem parâmetro, para ler um valor e chamar/criar OUTRA função (com parâmetro) que mostre se o valor é par ou ímpar.

def checagem(num):
    if num % 2 == 0:
        print('Número par.')
    else:
        print('Número ímpar.')
    
def ler():
    num = int(input('Insira um número: '))
    
    checagem(num)

def main():
    ler()

main()