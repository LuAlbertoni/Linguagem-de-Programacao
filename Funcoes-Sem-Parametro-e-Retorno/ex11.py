# Faça um programa contendo uma função/método que apresente o valor 1 se o número digitado for positivo e 0 se for negativo.

def checagem():
    num = int(input('Insira um número: '))
    
    if num % 2 == 0:
        print('1')
    else:
        print('0')

def main():
    checagem()

main()