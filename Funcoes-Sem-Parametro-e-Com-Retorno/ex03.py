# Faça um programa contendo uma função/método que leia a base e a altura de um triângulo e retorne/apresente sua área A = (base x altura)/2.

def calc():
    base = float(input('Insira a base: '))
    altura = float(input('Insira a altura: '))
    
    return (base * altura) / 2

def main():
    print(calc())

main()