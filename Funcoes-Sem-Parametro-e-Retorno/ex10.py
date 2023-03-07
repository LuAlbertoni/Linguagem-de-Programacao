# Faça uma função/método que leia um valor inteiro e positivo N e mostre o valor de S, obtido pelo seguinte cálculo:
# S = 1 + 1/1! + 1/2! + 1/3! + ... + 1/N!
# Observação: Não pode usar vetor e função pronta da linguagem Python.

def calculo():
    n = int(input('Digite um valor inteiro e positivo: '))
    
    s = 0
    
    for i in range(n + 1):
        if n == 0:
            fat = 1
        else:
            fat = 1
            while n > 0:
                fat = fat * n
                n = n - 1
                
            s = s + 1/fat

    print(f'O valor de S é: {s:.3f}')
    
def main():
    calculo()

main()