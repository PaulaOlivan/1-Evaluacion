# este programa se encarga de decirte si el numero introducido es primo o no
def numero_primo():
    print "Bienvenido a: Es tu numero primo?"
    print "El mejor programa de ordenador del mundo"
    primo = True
    numero = input ("Cual es su numero bello ser?")
    for i in range (2, numero):
       if (numero%i==0):
           primo=False
    if (primo==True):
        print "Es primo"
    else:
        print "No es primo"
numero_primo()
    
