# Faça um programa contendo algumas funções:

# a) Crie uma função para apresentar o menu e retornar a opção/número/cálculo escolhido.
# Menu de cálculos
# 1.   Número ao quadrado
# 2.   Número ao cubo
# 3.   Raiz do número
# 4.   Raiz cúbica do número
# Qual é a opção desejada?

# b) Desenvolva uma função para cada opção de cálculo.

# c) A função main() chamará todas as outras.

# Observação: Na chamada das funções deve-se utilizar uma estrutura de repetição, que permita diversos cálculos, quando o usuário quiser sair da calculadora digitará qualquer valor diferente dos números do menu.

def menu():
    print('# Menu de cálculos #\n1. Número ao quadrado\n2. Número ao cubo\n3. Raíz do número\n4. Raíz cúbica do número\n')
    
    return int(input('Insira a opção desejada: '))

def quad(num):
    return num * num

def cubo(num):
    return num * num * num

def raizQuad(num):
    return num ** 0.5

def raizCub(num):
    return num ** 0.33

def main():
    while True:
        num = int(input('Insira um número: '))
    
        while True:
            option = menu()
            
            if option == 1:
                result = quad(num)
            elif option == 2:
                result = cubo(num)  
            elif option == 3:
                result = raizQuad(num)
            elif option == 4:
                result = raizCub(num)
            else:
                break
            
            print(f'O resultado é {result:.2f}\n')
            
main()