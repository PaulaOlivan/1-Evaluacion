#este programa sirve para introducir un numero y decir si es par o impar.
def par_impar():
    print "Bienvenido al programa de numeros pares o impares"
    print "Introduce tu numero para comenzar"
    x= input ("Numero = ")
    if (x%2==0):
        print "tu numero es", "par"
    else:
        print "tu numero es", "impar"

par_impar()
