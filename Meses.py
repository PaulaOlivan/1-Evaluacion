#Este programa se encarga de decir el numero de la semana mediante el numero que el usuario mete
def dias_semana():
    print "Que numero de mes es?"
    x= input ("Que numero de mes es hoy: ")
    if (x==1):
        print "Estamos en enero"
    else:
        if (x==2):
            print "Estamos en febrero"
        else:
            if (x==3):
                print "Estamos en marzo"
            else:
                if (x==4):
                    print "Estamos en abril"
                else:
                    if (x==5):
                        print "Estamos en mayo"
                    else:
                        if (x==6):
                            print "Estamos en junio"
                        else:
                            if (x==7):
                                print "Estamos en julio"
                            else:
                                if (x==8):
                                    print "Estamos en agosto"
                                else:
                                    if (x==9):
                                        print "Estamos en septiembre"
                                    else:
                                        if (x==10):
                                            print "Estamos en octubre"
                                        else:
                                            if (x==11):
                                                print "Estamos en noviembre"
                                            else:
                                                if (x==12):
                                                    print "Estamos en diciembre"
                                                else:
                                                    if (x>=13):
                                                        print "Solo hay doce meses en el año, vuelve a primaria."

dias_semana()
