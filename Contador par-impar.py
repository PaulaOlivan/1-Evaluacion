#este programa se encargara de contar hasta 100 y decir que numeros son pares o impares
#ejercicio 1
def contador():
    print "Programa contador de numeros pares e impares"
    print "Hasta que numero quieres contar?"
    x= input("Numero mas alto:")
    for i in range(1,x+1): # lo que esta orden quiere decir es que i ira en un rango de el primer numero hasta el ultimo.
        if(i%2==0): #lo que va entre parentesis quiere decir que el resto (%) de la division de i entre 2 es igual a 0. Si cumple esto es par
            print "i= ", i, " es par"
        else:
            print "i= ", i, " es impar"
contador()
    
