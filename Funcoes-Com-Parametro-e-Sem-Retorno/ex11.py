# Faça uma função/método para verificar e contar quantas letras a tem numa frase. Não use NENHUMA função pronta da linguagem Python.

def checagem(frase):
    count = 0
    
    for i in frase:
        if i == 'a' or i == 'A':
            count += 1
            
    print(f'Há {count} letras "A"')

def main():
    frase = input('Insira a frase: ')
    
    checagem(frase)

main()