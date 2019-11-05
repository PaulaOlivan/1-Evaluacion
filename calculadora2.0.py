#este programa recibe dos numeros y se encarga de hacer la operacion deseada



def calculadora():
    print "Ha iniciado el programa de la calculadora"
    x= input ("Cual es el primer numero")
    y= input ("Cual es el segundo numero")
    repetir = True
    while(repetir==True):
        o= raw_input ("Elija la operacion deseada: s para sumas, r para restas, m para multiplicacion y d para division")
        if(o== 's' or o== 'r' or o== 'm' or o== 'd' ):
            repetir=False
            if (o=='d'):
                if (y==0):
                    print "Error, esta dividiendo por cero"
                    repetir=True
                else:
                    respuesta=x/y
            if (o=='s'):
                respuesta=x+y
            if (o=='r'):
                respuesta=x-y
            if (o=='m'):
                respuesta=x*y
            
    print respuesta
calculadora()
