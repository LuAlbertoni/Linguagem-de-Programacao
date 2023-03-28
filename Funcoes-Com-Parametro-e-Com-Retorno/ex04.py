# Faça um programa contendo uma função/método que receba duas notas (P1, P2) calcule a média, chame outra função na main que avalie se este aluno esta aprovado ou reprovado retornando a str/string 'Aprovado' ou 'Reprovado'.

def media(p1, p2):
    if (p1 + p2) / 2 >= 6:
        return 'Aprovado'
    else:
        return 'Reprovado'

def main():
    p1 = float(input('Insira a 1a nota: '))
    p2 = float(input('Insira a 2a nota: '))
    
    print(media(p1, p2))

main()