#En este programa pedimos al usuario
#que introduzca los coeficientes de un polinomio
#y hallamos el valor de las raices, es decir, igualar a cero.
def ecuacion():
    print "Introduzca los coeficientes del polinomio"
    print "Ax^2+Bx+C"
    A= input ("A= ")
    B= input ("B= ")
    C= input ("C= ")
    Radicando= B*B-4*A*C
    if (Radicando>=0):
        Raiz1= (-B+(Radicando)^1/2)/(2*A)
        Raiz2= (-B-(Radicando)^1/2)/(2*A)
        print "Primera solucion",Raiz1
        print "Segunda solucion",Raiz2
    else:
        print "Error, no existe solucion real"

ecuacion()
