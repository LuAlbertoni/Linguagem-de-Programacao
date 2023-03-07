# Faça uma função/método que calcule a média de um aluno que realizou duas provas (P1 e P2), a partir desta média, chame/crie OUTRA função que verifique se esta média aprova ou reprova o aluno.

def verificacao(media):
    if(media >= 6):
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')

def media(nota1, nota2):
    media = (nota1 + nota2) / 2
    
    verificacao(media)

def main():
    nota1 = float(input('Insira a 1a nota: '))
    nota2 = float(input('Insira a 2a nota: '))
    
    media(nota1, nota2)
    
main()