#  Preencha um vetor de 10 elementos de quantidade de produtos na função main(), crie uma função/método que a partir do vetor preenchido (parâmetro) verifique a quantidade mínima de estoque, quando encontrado algum menor que 3, avise por meio de uma mensagem.

def checagem(quant):
    for i in range(len(quant)):
        if quant[i] < 3:
            print('Há itens com baixo estoque.')

def main():
    quant = []
    
    for i in range(10):
        valor = int(input('Insira a quantidade disponível: '))
        
        quant.append(valor)
        
    checagem(quant)

main()