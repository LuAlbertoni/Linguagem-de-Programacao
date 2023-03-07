# Faça um programa contendo uma função/método para subtrair dois números e apresentar o resultado.

def subtracao(num1, num2):
    result = num1 - num2
    print(result)
    
def main():
    num1 = int(input('Insira um número: '))
    num2 = int(input('Insira um número: '))
    
    subtracao(num1, num2)

main()