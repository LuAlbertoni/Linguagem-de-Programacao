# Faça uma função/método retorne um vetor com os três primeiros números perfeitos. Sabe-se que um número é perfeito quando é igual a soma de seus divisores (exceto ele mesmo).
# Exemplo: os divisores de 6 são 1, 2 e 3, e 1 + 2 + 3 = 6, logo 6 é perfeito. Não use função pronta.

# 1º número perfeito: 6
# 2º número perfeito: 28
# 3º número perfeito: 496

def check():
    arrayPerfect = []
    
    for i in range(1, 497):

        result = 0
       
        for j in range(1, i):
            if i % j == 0:
                result += j
                
        if result == i:
            arrayPerfect.append(i)
            
    return arrayPerfect

def main():
    print(check())
    
main()