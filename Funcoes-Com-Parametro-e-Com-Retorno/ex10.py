# Crie uma função que verifique se um número é divisível por outro. Use o caracter %.

def rest(num1, num2):
    if num1 % num2 == 0:
        return 'Divisível'
    else:
        return 'Não divisível'
    
def main():
    num1 = int(input('Insira o 1o número: '))
    num2 = int(input('Insira o 2o número: '))
    
    print(rest(num1, num2))

main()