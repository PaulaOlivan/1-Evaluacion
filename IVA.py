#programa encargado de recibir un precio y tipo de iba, y devolver el precio final.
def IVA():
    print "Bienvenido al calculador automatico de IVA"
    p = input ("Cuanto vale su producto?")
    repetir = True
    while(repetir==True):
        i= raw_input ("Elija el IVA: g para general, r para reducido, s para superreducido: ")
        if(i== 'g' or i=='r' or i=='s'):
            repetir = False
            if (i=='g'):
                respuesta = (p+(p*0.16))
            if (i=='r'):
                respuesta = (p+(p*0.07))
            if (i=='s'):
                respuesta = (p+(p*0.04))
    print respuesta, "€"
    repetir= True
IVA()
                
