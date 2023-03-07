# Faça um programa contendo uma função/método que leia um número e o multiplique por 2, apresente o resultado.

def multiplicacao(num):
    num *= 2
    print(num)

def main():
    num = int(input('Insira um número: '))
    multiplicacao(num)
    
main()