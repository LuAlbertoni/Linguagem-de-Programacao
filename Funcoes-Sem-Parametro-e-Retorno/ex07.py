# Faça uma função/método que leia três notas de um aluno e uma letra, se a letra for igual a A, deverá calcular a média aritimética das notas dos alunos, se for P, deverá calcular a média ponderada, com pesos 5, 3 e 2. A média deve ser mostrada ao final.

# N1, N2 e N3 são notas.
# P1, P2 e P3 são pesos.
# Média ponderada = (N1 * P1 + N2 * P2 + N3 * P3 ) / (P1 + P2 + P3)

def media():
    n1 = float(input('Insira a 1a nota: '))
    n2 = float(input('Insira a 2a nota: '))
    n3 = float(input('Insira a 3a nota: '))
    
    while True:
        letra = input('Insira uma letra (A: Média Aritmética | P: Média Ponderada): ')
        
        if letra == 'A' or letra == 'P':
            break
        else:
            print('Letra inválida, tente novamente.')
            
    if letra == 'A':
        media = (n1 + n2 + n3)/3
    elif letra == 'P':
        media = (n1 * 5 + n2 * 3 + n3 * 2 ) / (5 + 3 + 2)
        
    print(media)
    
def main():
    media()
    
main()