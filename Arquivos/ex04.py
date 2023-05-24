# Baixe o arquivo futebol.txt que esta na pasta Material do aula do Teams. Leia este arquivo e o apresente. Com os dados lidos, armazene na estrutura Futebol (posicao_jogo, altura, peso, imc), calcule o IMC (Índice de Massa Corporal), armazene na estrutura e também em outro arquivo, mas agora chamado futebol_imc.txt. Apresente este novo arquivo.

class classeFutebol():
    posicao_jogo = ''
    altura = 0
    peso = 0
    imc = 0

def cadastro():
    arquivo = open('futebol.txt', 'r')
    arquivo_imc = open('futebol_imc.txt', 'w')
    
    for jogador in arquivo.readlines():
        jogador = jogador.strip().split(',')
        posicao_jogo, altura, peso = jogador
        
        imc = float(peso) / (float(altura) ** 2)
        
        arquivo_imc.write(f'{posicao_jogo};{altura};{peso};{imc:.2f}\n')
    
    arquivo.close()
    arquivo_imc.close()
    
def visualizar():
    arquivo_imc = open('futebol_imc.txt', 'r')
    
    for jogador in arquivo_imc.readlines():
        jogador = jogador.strip().split(';')
        posicao_jogo, altura, peso, imc = jogador
        
        print(f'Posição de jogo: {posicao_jogo}\nAltura: {altura}\nPeso: {peso}\nIMC: {imc}\n')
    
    arquivo_imc.close()

def main():
    cadastro()

    visualizar()

main()