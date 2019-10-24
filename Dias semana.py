#Este programa se encarga de decir el numero de la semana mediante el numero que el usuario mete
def dias_semana():
    print "Que dia de la semana es?"
    x= input ("Que dia de la semana es hoy: ")
    if (x==1):
        print "Hoy es lunes"
    else:
        if (x==2):
            print "Hoy es martes"
        else:
            if (x==3):
                print "Hoy es miercoles"
            else:
                if (x==4):
                    print "Hoy es jueves"
                else:
                    if (x==5):
                        print "Hoy es viernes"
                    else:
                        if (x==6):
                            print "Hoy es sabado"
                        else:
                            if (x==7):
                                print "Hoy es domingo"
                            else:
                                if (x>=8):
                                    print "Idiota, la semana no tiene tantos dias"

dias_semana()
