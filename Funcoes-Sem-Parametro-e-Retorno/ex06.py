# Faça uma função/método que leia um valor inteiro entre 1 e 9 e mostre a seguinte tabela de multiplicação:
# Neste exemplo foi escolhido o número 9.
# 1    
# 2     4
# 3     6     9
# 4     8    12    16
# 5    10    15    20    25
# 6    12    18    24    30    36
# 7    14    21    28    35    42    49
# 8    16    24    32    40    48    56    64   
# 9    18    27    36    45    54    63    72    81

def calc():
    while True:
        num = int(input('Insira um número entre 1 e 9: '))
        
        if num >= 1 and num <= 9:
            break
        else:
            print('Número inválido.')
            
    for i in range(1, num + 1):
        for j in range(i + 1):
            if j > 0:
                print(f'{i * j}', end='\t')
        print('\n')

def main():
    calc()

main()