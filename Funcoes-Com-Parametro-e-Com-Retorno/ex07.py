# Faça um programa contendo algumas funções:
# a) Crie uma função para apresentar o menu e retornar caracter do cálculo escolhido.

# *** Minha Calculadora ***

# Digite um número.....: 
# Digite outro número..: 
#     + Soma dois números
#     - Subtrai dois números
#     * Multiplica dois números
#     / Divide dois números
# Qual opção deseja? 

# b) Desenvolva uma função para cada opção de cálculo, mas estas não terão retorno.

# c) A função main() chamará todas as outras, passando a elas os valores digitados dos dois números.

# Observação: Na chamada da função deve-se utilizar uma estrutura de repetição que permita diversos cálculos, quando o usuário quiser sair da calculadora digitará qualquer valor diferente dos caracteres do menu.

def menu():
    print('*** Minha Calculadora ***\n+ Soma dois números\n- Subtrai dois números\n* Multiplica dois números\n/ Divide dois números')
    
    return input('Insira a opção desejada: ')

def soma(num1, num2):
    print(f'\nResultado é {num1 + num2}\n')

def sub(num1, num2):
    print(f'\nResultado é {num1 - num2}\n')
    
def mult(num1, num2):
    print(f'\nResultado é {num1 * num2}\n')
    
def div(num1, num2):
    print(f'\nResultado é {num1 / num2}\n')

def main():
    while True:
        num1 = int(input('Insira o 1o número: '))
        num2 = int(input('Insira o 2o número: '))
        
        while True:
            option = menu()
            
            if option == '+':
                soma(num1, num2)
            elif option == '-':
                sub(num1, num2)
            elif option == '*':
                mult(num1, num2)
            elif option == '/':
                div(num1, num2)
            else:
                break

main()