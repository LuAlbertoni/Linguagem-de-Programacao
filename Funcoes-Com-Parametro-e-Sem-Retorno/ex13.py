# Preencha dois vetores de 10 elementos, um de nome de funcionário e outro com quantidade de filhos na função main(), crie uma função/método que a partir dos vetores preenchido (parâmetro) verifique se ocorreu nascimento de filho e de que funcionário é. Crie outra função que fará a inserção de mais um filho para este funcionário no vetor, apresente após a verificação a relação de nomes de funcionários e a quantidade de filhos de todos.

def resultados(nomeFunc, quantFilhos):
    for i in range(len(nomeFunc)):
        print(f'{nomeFunc[i]} possui {quantFilhos[i]} filhos.')

def insercao(nomeFunc, quantFilhos):
    while True:
        nome = input('Insira o nome do funcionário: ')
    
        for i in range(len(nomeFunc)):
            if nomeFunc[i] == nome:
                quantFilhos[i] += 1
                
        question = input('Há mais atualizações? (S/N) ')
        
        if question != 'S' and question != 's':
            break
        
            
    resultados(nomeFunc, quantFilhos)

def checagem(nomeFunc, quantFilhos):
    resposta = input('Ocorreu nascimento? (S/N) ')
    
    if resposta == 'S' or resposta == 's':
        insercao(nomeFunc, quantFilhos)
    else:
        resultados(nomeFunc, quantFilhos)

def main():
    nomeFunc = []
    quantFilhos = []
    
    for i in range(10):
        nome = input('Insira o nome do funcionário: ')
        filhos = int(input('Insira a quantidade de filhos: '))
        
        nomeFunc.append(nome)
        quantFilhos.append(filhos)
        
    checagem(nomeFunc, quantFilhos)

main()