# Faça um programa contendo uma função/método que leia um número e o multiplique por 2. Apresente o resultado. EXEMPLO.

#definição da função
def multiplicar():
    numero = int(input('Digite o número: '))
    print('O resultado é', numero * 2)

def main():
    #chamada da função multiplicar
    multiplicar()

#chamada da função main()
main()