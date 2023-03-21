# Preencha um vetor de 10 elementos de nome de shopping e outro vetor de mesmo tamanho com o faturamento de alguns meses na função main(), por exemplo, o shopping centro, pode ter mais que um lançamento, neste caso some os que for deste e apresente o total. Crie uma função/método que a partir dos vetores preenchidos (parâmetros) calcule e apresente o faturamento total de cada shopping.

def resultados(arrayShopping, arrayFaturamento):
    for i in range(len(arrayShopping)):
        print(f'{arrayShopping[i]} faturou R$ {arrayFaturamento[i]:.2f}')

def checagem(nome, arrayShopping, arrayFaturamento):
    nomeEncontrado = -1
    
    for i in range(len(arrayShopping)):
        if arrayShopping[i] == nome:
            nomeEncontrado = i
    
    if nomeEncontrado != -1:
        faturamento = float(input(f'Shopping já salvo, insira o faturamento: '))
        arrayFaturamento[nomeEncontrado] += faturamento
    else:
        arrayShopping.append(nome)
        faturamento = float(input('Insira o faturamento: '))
        arrayFaturamento.append(faturamento)

def main():
    arrayShopping = []
    arrayFaturamento = []
    
    for i in range(10):
        nome = input('Insira o nome do shopping: ')
        
        checagem(nome, arrayShopping, arrayFaturamento)

    resultados(arrayShopping, arrayFaturamento)
    
main()