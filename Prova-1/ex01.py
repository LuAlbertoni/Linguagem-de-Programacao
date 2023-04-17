# Utilize a função main() para a chamada da função. Implemente uma função/método/sub-rotina que receba como parâmetro dois valores X e Z, calcule e mostre o resultado de XZ, SEM utilizar funções ou operadores de potência prontos.

def calc(x, z):
    result = x

    for i in range(z - 1):
        result *= x

    return result


def main():
    x = int(input('Insira o valor de X: '))
    z = int(input('Insira o valor de Z: '))

    print(calc(x, z))

main()