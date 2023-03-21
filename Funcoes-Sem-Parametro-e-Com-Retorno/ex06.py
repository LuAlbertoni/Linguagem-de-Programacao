# Faça um programa contendo uma função/método que verifique se um número é par, retorne/mostre o valor bool True para par e False para ímpar.

def check():
    num = int(input('Insira um número: '))
    
    if num % 2 == 0:
        return True
    else:
        return False

def main():
    print(check())

main()