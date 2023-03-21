# Faça um programa contendo uma função/método que verifique se um número é par, retorne mostrando a str/string ‘É par’ ou se ‘É ímpar’.

def check():
    num = int(input('Insira um número: '))
    
    if num % 2 == 0:
        return 'É par'
    else:
        return 'É ímpar'

def main():
    print(check())

main()