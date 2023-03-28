# Faça um programa contendo uma função/método que receba dois números via parâmetro, some os dois valores, retorne e apresente o resultado.

def calc(num1, num2):
    return num1 + num2

def main():
    num1 = int(input('Insira um número: '))
    num2 = int(input('Insira um número: '))
    
    print(calc(num1, num2))
    
main()