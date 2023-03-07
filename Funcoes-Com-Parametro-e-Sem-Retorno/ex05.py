# Faça uma função/método para a partir de um valor inicial e um valor final realizar o acumulo desse valores e apresentar o resultado. Não use vetor.

def acumulo(num1, num2):
    soma = 0
    
    if num1 < num2:
        for i in range(num1, num2 + 1):
            soma += i
    else:
        for i in range(num2, num1 + 1):
            soma += i
            
    print(f'A soma dos números é {soma}')

def main():
    num1 = int(input('Insira um número: '))
    num2 = int(input('Insira um número: '))

    acumulo(num1, num2)
    
main()