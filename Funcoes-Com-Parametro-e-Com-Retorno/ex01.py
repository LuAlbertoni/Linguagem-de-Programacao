# Faça um programa contendo uma função/método que receba por parâmetro um número e o multiplique por 2, retorne e apresente o resultado da função.

def calc(num):
    return num * 2

def main():
    num = int(input('Insira um número: '))
    
    print(calc(num))

main()