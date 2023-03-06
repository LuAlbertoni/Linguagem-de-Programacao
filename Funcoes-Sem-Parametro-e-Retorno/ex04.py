# Faça uma função/método que leia um único valor representado em segundos, converta-o e apresente o resultado em horas, minutos e segundos.

def conversao():
    seconds = int(input('Insira os segundos: '))
    
    print(f'Horas: {int(seconds/3600)}. Minutos: {int(seconds/60)}. Segundos: {seconds}')
    
def main():
    conversao()
    
main()