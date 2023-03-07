# Faça uma função/método para calcular a tabuada de um número informado pelo usuário.

def tabuada(num):
    for i in range(10):
        print(f'{i + 1} x {num} = {num * (i + 1)}')

def main():
    num = int(input('Insira um número: '))
    
    tabuada(num)
    
main()