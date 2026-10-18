import time
def ejecucion():
    print("=================================================================================================================")
    print("\tBienvenido este programa utiliza el metodo de la bisección para aproximar ciertas cosas\n\n")
    menu1()
    inferior = Decimal(input("Ingrese el intervalo inferior\n"))
    superior = Decimal(input("Ingrese el intervalo superior\n"))
    procesoaproximacion(inferior,superior)

def menu1():
    print("Hay actualmente 1 opción en el menu asi que es ineccesario elegir")
    print("Lo que hace la opción 1 es calcular una aproximacion para x ala x = 7")
    print("recomiendo poner el intervalo 2 a 3 o algun intervalo más abierto que incluya estos numeros pero que sea mayor que cero\n")


def imprimirerroractual(ea):
    print("\nEl error actual es de ",ea,"%")

def imprimirintervaloactual(xi,xf):
    print("El intervalo inferior es de: ", xi)
    print("Y el superior: ",xf)
    
def imprimirvaloractualaprox(xm):
    print("El valor total aprox actual es de ",xm)
    
def imprimirinformacionbasica(ea,xi,xf,xm):
    imprimirerroractual(ea)
    imprimirintervaloactual(xi,xf)
    imprimirvaloractualaprox(xm)
    
def imprimirfinal(xm,ea,e,i):
    print("\n\n\tse ha llegado al final del programa por que se llego al error pedido\n\to porque el valor medio es una raiz de la funcion pedida")
    print("\n\n===================================================================================================")  
    if(f(xm,1)==0):
        print(xm ,"es exactamente una raiz de la función")
    else:
        print("\n\nLa aproximación final tiene un error de", ea, "%, ""es decir,", (e-ea), "puntos porcentuales por debajo ","del error máximo permitido.")
        print("El valor aproximado de la raiz es " ,xm)
    print("el programa finalizo en ",i, " iteraciones muchas gracias por haberlo usado")
    print("\n\n===================================================================================================")

def imprimiriteracion(i, ea, xi, xf, xm):
    print("\n========== ITERACIÓN", i, "==========")
    imprimirinformacionbasica(ea, xi, xf, xm)
    print("\n================================")
         
def cambiarxm(xi,xf):
    return (xi+xf)/2
    

def procesoaproximacion(xi,xf):
    xm=cambiarxm(xi,xf)
    error = Decimal(input("Ingrese el error que desea que tenga su aproximación:"))
    errora=1000
    i=0

    while(errora > error or f(xm,1)==0):
        i+=1

        if(f(xi,1)*f(xm,1)<0):
            xf=xm
            xm=cambiarxm(xi,xf)
            errora=errorabsoluto(xi,xf)

        elif(f(xi,1)*f(xm,1)>0):
            xi=xm
            xm=cambiarxm(xi,xf)
            errora=errorabsoluto(xi,xf)
            
        imprimiriteracion(i, errora, xi, xf, xm)
        if(f(xm,1)==0):
            break

        time.sleep(5)

    imprimirfinal(xm,errora,error,i)

   
