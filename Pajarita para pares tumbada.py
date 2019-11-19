#Programa que hace una pajarita
def pajarita():
    altura = input ("Cual es la altura total de tu pajarita (numero par): ")
    espacios = '*'
    asteriscos = ' '
    for i in range (altura/2):
        for nespacios in range (0,i):
            espacios = espacios + '*'
        for nasteriscos in range (0,altura-1-2*i-1):
            asteriscos = asteriscos + ' '
        print espacios + asteriscos
        espacios = '*'
        asteriscos = ' '
    for i in range(altura/2):
        for nespacios in range(1, (altura/2)-i):
            espacios = espacios + '*'            
        for nasteriscos in range(1,2*i+1):
            asteriscos = asteriscos + ' '
        print espacios + asteriscos + espacios
        espacios = '*'
        asteriscos = ' '

pajarita()
