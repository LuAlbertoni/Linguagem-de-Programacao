# Faça uma função/método que receba três números inteiros a, b, c que sejam divisíveis por a. Os valores b e c representam o intervalo da estrutura de repetição. Apresente a quantidade e os números divisíveis. Não pode usar vetor e função pronta da linguagem Python.

def resolve():
    a = int(input('Insira um número: '))

    b = int(input(f'Insira um número divisível por {a}: '))
    c = int(input(f'Insira mais um número divisível por {a}: '))
            
    if b < c:
        for i in range(b, c + 1):
            if i % a == 0:
                print(f'{i} é divisível por {a}')
    else:
        for i in range(c, b + 1):
            if i % a == 0:
                print(f'{i} é divisível por {a}')

def main():
    resolve()

main()