# Utilize a função main() para a chamada da função. Na main digite o valor necessário para esta lógica. Faça uma função/método/sub-rotina que receba como parâmetro um valor inteiro e positivo N, indicando a quantidade de parcelas de uma soma S, calculada pela fórmula:
# S = 2/3 + 5/4 + 10/5 + 17/6 + 26/7 + ... + N
# Apresente o resultado.
# Neste exemplo, N (quantidade de parcelas) é igual a 5.
# O início deve ser 2 e 3 como mostrado no exemplo.

def calc(n):
    soma = 2/3

    for i in range(3, n + 2):
        soma += (((i - 2) * (i - 1)) + i)/(i + 1)

    return soma

def main():
    n = int(input('Insira a quantidade de parcelas: '))

    print(f'Resultado: {calc(n):.3f}')

main()