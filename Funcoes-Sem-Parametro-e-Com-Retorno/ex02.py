# Faça um programa contendo uma função/método para subtrair dois números, retornar o resultado e o apresentando.

def numbers():
    num1 = float(input('Insira um número: '))
    num2 = float(input('Insira um número: '))
    return num1 - num2

def main():
    print(numbers())

main()