# Faça um programa contendo uma função/método que receba um valor de porcentagem de aumento e um salário via parâmetro, aplique este aumento ao salário do funcionário. Na parte principal (main) do programa, na chamada da função, utilize um laço de repetição para ler 10 salários, chame a função para aplicar o aumento e gerar o novo salário, ainda dentro da estrutura de repetição acumule os novos salários e ao final apresente quanto será gasto no novo salário. Também apresente qual será a diferença entre o que se pagava para todos os funcionário e o que será pago após o aumento.

def calc(salArray, aumArray):
    newSalArray = []
    
    for i in range(len(salArray)):
        newSal = salArray[i] + (salArray[i] * aumArray[i]) / 100
        
        newSalArray.append(newSal)
    
    return newSalArray

def main():
    salArray = []
    aumArray = []
    salOld =  0
    salNew = 0
    
    for i in range(10):
        sal = float(input('Insira o salário: '))
        aum = float(input('Insira a porcentagem de aumento: '))
        
        salArray.append(sal)
        aumArray.append(aum)
        
    newSalArray = calc(salArray, aumArray)
        
    for i in range(10):
        print(f'Novo salário: R$ {newSalArray[i]}. Diferença do antigo salário: R$ {newSalArray[i] - salArray[i]}')
        
        salOld += salArray[i]
        salNew += newSalArray[i]
    
    print(f'A diferença total será de R$ {salNew - salOld}')    

main()