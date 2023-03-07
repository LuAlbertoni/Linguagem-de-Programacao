# Faça uma função/método para verificar se um nome digitado é igual a ‘Ana’, mostre o valor True ou False como resposta.

def checagem(nome):
    if nome == 'Ana':
        print(True)
    else:
        print(False)

def main():
    nome = input('Insira um nome (case sensitive): ')
    checagem(nome)
    
main()