# Faça uma função/método que leia cinco valores inteiros, determine e mostre o maior e o menor deles. Não pode usar vetor e função pronta da linguagem Python.

def ordem():
    num1 = int(input('Insira um número inteiro: '))
    num2 = int(input('Insira um número inteiro: '))
    num3 = int(input('Insira um número inteiro: '))
    num4 = int(input('Insira um número inteiro: '))
    num5 = int(input('Insira um número inteiro: '))
    
    maior = num1
    menor = num1
    
    if maior < num2:
        maior = num2
    if maior < num3:
        maior = num3
    if maior < num4:
        maior = num4
    if maior < num5:
        maior = num5
        
    if menor > num2:
        menor = num2
    if menor > num3:
        menor = num3
    if menor > num4:
        menor = num4
    if menor > num5:
        menor = num5
        
    print(f'Maior número é {maior} e o menor é {menor}')

def main():
    ordem()

main()