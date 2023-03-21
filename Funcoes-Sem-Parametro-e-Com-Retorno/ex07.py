# Faça uma função/método que leia e armazene 5 elementos inteiros no vetor A, deverá ser gerado um vetor B, de mesmo tamanho, que armazenará o fatorial de cada elemento de A. Não use função pronta de cálculo de fatorial. Retorne/apresente o vetor B.

def fat():
    array = []
    arrayFat = []
    
    for i in range(5):
        num = int(input('Insira um número: '))
        
        array.append(num)
        
    for i in range(len(array)):
        result = 1
        
        for j in range(array[i]):
            result *= j + 1
            
        arrayFat.append(result)
        
    return arrayFat
        
def main():
    print(fat())

main()