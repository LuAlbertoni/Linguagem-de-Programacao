# Faça uma função/método que leia dois valores positivos e apresente a soma dos N números existentes entre eles (inclusive).

def num_existentes():
    num1 = int(input('Insira o 1o número: '))
    num2 = int(input('Insira o 2o número: '))
    
    soma = 0
    
    if num1 < num2:
        for i in range(num1, num2 + 1):
            soma += i
    else:
        for i in range(num2, num1 + 1):
            soma += i
            
    print(f'A soma dos números é {soma}')

def main():
    num_existentes()
    
main()