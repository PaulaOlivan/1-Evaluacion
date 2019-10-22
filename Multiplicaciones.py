#Este programa multiplica 4 numeros distintos de cero
def multiplicacion():
    print "Cualculadora de multiplicaciones"
    a= input("Primer factor")
    b= input("Segundo factor")
    c= input("Tercer factor")
    d= input("Cuarto factor")
    if (a==0):
        print "El resultado es 0"
    else:
        if (b==0):
            print "El resultado es 0"
        else:
            if (c==0):
                print "El resultado es 0"
            else:
                if (d==0):
                    print "El resultado es 0"
                else:
                    print "Su resultado es", a*b*c*d
    

multiplicacion()
