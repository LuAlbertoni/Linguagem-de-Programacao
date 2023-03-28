# Na função main() o usuário deverá informar a quantidade de linhas e colunas, crie/chame uma função para criar e digitar os elementos de uma matriz, retorne-a. Crie/chame outra função que a calculará a soma de todas as linhas e armazenará num vetor do tamanho da quantidade de linhas, retorne-o e apresente na main().

def criarMatriz(linhas, colunas):
    matriz = []
    
    for i in range(linhas):
        linha = []
        
        for j in range(colunas):
            elemento = int(input(f"Digite o elemento da linha {i+1}, coluna {j+1}: "))
            linha.append(elemento)
            
        matriz.append(linha)
        
    return matriz

def calcularSomaLinhas(matriz):
    somaLinhas = []
    
    for linha in matriz:
        soma = sum(linha)
        somaLinhas.append(soma)
        
    return somaLinhas

def main():
    linhas = int(input("Digite a quantidade de linhas da matriz: "))
    colunas = int(input("Digite a quantidade de colunas da matriz: "))

    matriz = criarMatriz(linhas, colunas)
    somaLinhas = calcularSomaLinhas(matriz)
    
    print(f"Matriz digitada: {matriz}")
    print(f"Soma das linhas: {somaLinhas}")

main()