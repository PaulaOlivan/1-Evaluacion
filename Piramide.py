def piramide():
    espacios = ' '
    asteriscos = '*'
    filas = input ("Cual es la altura de la piramide: ")
    for i in range (filas):
        for nespacios in range(filas-i-1):
            espacios = espacios + ' '
        for nasteriscos in range (2*i):
            asteriscos = asteriscos + '*'
        print espacios + asteriscos
        espacios = ' '
        asteriscos = '*'
piramide()
