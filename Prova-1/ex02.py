# Utilize a função main() para a chamada da função. Na main digite os valores da matriz. Implemente uma função/método que receba como parâmetro uma matriz 3x5, armazene os seus elementos num vetor de 15 elementos, retorne-o para a main e apresente todos os seus elementos, utilizando a estrutura de repetição while. Não será aceito o for.

def vet(matriz):
    vetor = []

    for i in range(3):
        for j in range(5):
            vetor.append(matriz[i][j])

    return vetor

def main():
    matriz = []
    
    for i in range(3):
        linha = []
        
        for j in range(5):
            elemento = int(input(f"Digite o elemento da linha {i + 1}, coluna {j + 1}: "))
            linha.append(elemento)
            
        matriz.append(linha)
        
    vetor = vet(matriz)

    i = 0
    j = 0
    count = 0

    while True:
        print(f'Valor da linha {i + 1}, coluna {j + 1}: {vetor[count]}')

        count += 1
        j += 1

        if count == len(vetor):
            break
        elif j == 5:
            i += 1
            j = 0

main()