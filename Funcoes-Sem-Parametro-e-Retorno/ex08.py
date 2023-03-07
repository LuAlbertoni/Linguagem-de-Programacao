# Faça uma função/método que leia uma hora de início e de término de um jogo, ambas divididas em dois valores distintos: hora e minuto. Deverá ser apresentado a duração expressa em minutos, considerando que o tempo máximo de duração de um jogo é de 24 horas e que ele pode começar em um dia e terminar no outro.

def horario():
    horaInicio = int(input('Insira a hora de início: '))
    minInicio = int(input('Insira os minutos de início: '))
    horaTermino = int(input('Insira a hora de término: '))
    minTermino = int(input('Insira os minutos de término: '))
    
    if horaInicio > horaTermino:
        tempoTotal = (24 - horaInicio) + horaTermino
    else:
        tempoTotal = horaTermino - horaInicio
        
    if minInicio < minTermino:
        tempoTotal *= 60
        tempoTotal += minInicio - minTermino
    else:
        tempoTotal -= 1
        tempoTotal *= 60
        tempoTotal += (60 - minInicio) + minTermino
        
    print(tempoTotal)
       
def main():
    horario()

main()