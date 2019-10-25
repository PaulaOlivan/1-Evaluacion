#este programa se encarga de recibir los numeros de una fecha y devolver la fecha con meses
def fecha():
    print "Este programa se encargara de devolver la fecha de hoy a partir de los numeros de la misma"
    d= input ("Que numero del mes es hoy?")
    m= input ("Que numero de mes es?")
    a= input ("En que año estamos?")
    for m in range (1,12):
        if (m==1):
            m= "Enero"
        if (m==2):
            m= "Febrero"
        if (m==3):
            m= "Marzo"
        if (m==4):
            m= "Abril"
        if (m==5):
            m= "Mayo"
        if (m==6):
            m= "Junio"
        if (m==7):
            m= "Julio"
        if (m==8):
            m= "Agosto"
        if (m==9):
            m= "Septiembre"
        if (m==10):
            m= "Octubre"
        if (m==11):
            m= "Noviembre"
        if (m==12):
            m= "Diciembre"
        if (m>=13):
            m= "Error en el mes"
        if (d>=31):
            d= "Error en el dia"
    print "Hoy es", d, m, a

fecha()
