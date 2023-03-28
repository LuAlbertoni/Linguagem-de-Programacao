# Faça um programa contendo uma função/método que receba um valor de porcentagem de aumento via parâmetro, aplique este aumento a um salário de um funcionário, retorne e apresente o novo salário.

def calc(sal, aum):
    return sal + (sal * aum) / 100

def main():
    sal = float(input('Insira o salário atual: '))
    aum = float(input('Insira a porcentagem de aumento: '))
    
    print(calc(sal, aum))

main()