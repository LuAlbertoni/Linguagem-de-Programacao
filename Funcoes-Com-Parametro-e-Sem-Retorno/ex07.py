# Faça uma função/método para calcular a tabuada de um intervalo informado pelo usuário, por exemplo, tabuada do 3 ao 8.

def tabuada(num, inicio, final):
    for i in range(inicio, final + 1):
        print(f'{i} x {num} = {num * i}')

def main():
    num = int(input('Insira um número: '))
    inicio = int(input('Insira o início da tabuada: '))
    final = int(input('Insira o final da tabuada: '))
    
    tabuada(num, inicio, final)

main()