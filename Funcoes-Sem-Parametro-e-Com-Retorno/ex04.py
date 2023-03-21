# Faça um programa contendo uma função/método que leia o lado de um quadrado e retorne sua área, area = lado².

def calc():
    lado = float(input('Insira o lado do quadrado: '))
    
    return lado * lado

def main():
    print(calc())

main()