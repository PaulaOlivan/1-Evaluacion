#Programa que hace una pajarita
def pajarita():
    altura = input ("Cual es la altura total de tu pajarita(6 o 7): ")
    espacios = ' '
    asteriscos = '*'
    for i in range (altura/2):
        for nespacios in range (altura/2-i-1,altura/2+2):
            espacios = espacios + ' '
        for nasteriscos in range (2*i,altura/2+1):
            asteriscos = asteriscos + '*'
        print espacios + asteriscos
        espacios = ' '
        asteriscos = '*'
    for i in range (altura/2):
        for nespacios in range (altura-i-(altura-5)):
            espacios = espacios + ' '
        for nasteriscos in range (2*i):
            asteriscos = asteriscos + '*'
        print espacios + asteriscos
        espacios = ' '
        asteriscos = '*'

pajarita()
