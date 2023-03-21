# Foi realizada uma pesquisa sobre algumas características físicas de cinco habitantes de uma região. Foram coletados os seguintes dados de cada habitante: idade, sexo (M - masculino ou F - feminino), cor dos olhos (A - azuis ou C - castanhos), cor dos cabelos (L - louros, P - pretos ou C - castanhos).
# Faça uma função/método que leia esses dados, armazenando-os em vetores (listas);
# Faça uma função/método que determine e devolva a função principal a média de idades das pessoas com olhos castanhos e cabelos pretos;
# Faça uma função/método que determine e devolva a função principal a maior idade entre os habitantes;
# Faça uma função/método que determine e devolva a função principal a quantidade de indivíduos do sexo feminino com idade entre 18 e 35 anos(inclusive) e que tenham olhos azuis e cabelos louros.

def cadastro():
    idadeArray = []
    sexoArray = []
    olhosArray = []
    cabelosArray = []
    
    mediaIdade = 0
    mediaIdadeQuant = 0
    maiorIdade = 0
    quantIndividuos = 0
    
    quant = int(input('Insira a quantidade total de habitantes: '))
    
    for i in range(quant):
        idade = int(input('Insira a idade: '))
        sexo = input('Insira o sexo (M ou F): ')
        olhos = input('Insira a cor dos olhos: ')
        cabelos = input('Insira a cor dos cabelos: ')
        
        idadeArray.append(idade)
        sexoArray.append(sexo)
        olhosArray.append(olhos)
        cabelosArray.append(cabelos)
        
    for i in range(len(idadeArray)):
        # Média idade cabelo preto e olhos castanhos
        if olhosArray[i] == 'Castanho':
            if cabelosArray[i] == 'Preto':
                mediaIdade += idadeArray[i]
                mediaIdadeQuant += 1
                
        # Mais velho
        if idadeArray[i] > maiorIdade:
            maiorIdade = idadeArray[i]
        
        # Feminino, olhos azuis, cabelos loiros, idade entre 18 e 35
        if sexoArray[i] == 'F':
            if idadeArray[i] >= 18 and idadeArray[i] <= 35:
                if olhosArray[i] == 'Azul':
                    if cabelosArray[i] == 'Loiro':
                        quantIndividuos += 1
                        
    if mediaIdadeQuant > 0:
        mediaIdade /= mediaIdadeQuant
        
    return f'Idade média: {mediaIdade}. Maior idade é {maiorIdade}. Quantidade do sexo feminino, olhos azuis, cabelos loiros e idade entre 18 e 35 anos é: {quantIndividuos}'

def main():
    print(cadastro())

main()