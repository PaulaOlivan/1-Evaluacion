#Pedir que se introduzca un numero y decir si el numero es par impar y si es multiplo de tres o no.
def par_impar_multiplo():
    print "Este programa se encargara de decirle si su numero es par o impar, ademas de decir si es multiplo de tres"
    print "Introduzca su numero para comenzar"
    x= input ("Su numero es ")
    if (x%2==0):
        if (x%3==0):
            print "su numero es", "par", "multiplo de tres"
        else:
            print "su numero es", "par", "no es multiplo de tres"
    else:
        if (x%3==0):
            print "su numero es", "impar", "multiplo de tres"
        else:
            print "su numero es", "impar", "no es multiplo de tres"

par_impar_multiplo()

