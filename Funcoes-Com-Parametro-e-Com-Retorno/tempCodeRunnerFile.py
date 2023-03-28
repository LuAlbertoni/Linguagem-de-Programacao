def calc(x1, x2, y1, y2):
    return (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5

def main():
    x1 = int(input('Insira a posição de x1: '))
    y1 = int(input('Insira a posição de y1: '))
    x2 = int(input('Insira a posição de x2: '))
    y2 = int(input('Insira a posição de y2: '))

    print(calc(x1, x2, y1, y2))
    
main()