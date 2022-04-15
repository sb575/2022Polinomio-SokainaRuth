
from polinomio import calc

calculo = calc()

def menu():
    print("*******       CALCULADORA       *******")
    print("*  Selecciona una opcion:             *")
    print("*  1. Suma                            *")
    print("*  2. Resta                           *")
    print("*  0. Salir                           *")
    print("***************************************")
    
    opcion = input("Opcion: ")


    try:
        if int(opcion) >= 0 and int(opcion) <= 2:
            return(int(opcion))
        else:
            print("Opcion incorrecta, por favor ingrese una opcion (1 para sumar y 2 para restar): ")
            return(int(input("Opcion: ")))
    except:
        print("Opcion incorrecta, por favor ingrese una opcion (1 para sumar y 2 para restar): ")
        return(int(input("Opcion: ")))

while(True):
    opcion = menu()

    if opcion == 0:
        print("Fin")
        break

    else:
        
        num11 = int(input("Ingrese el numero de elementos del primer polinomio: ")) 
        num22 = int(input("Ingresa el numero de elementos del segundo polinomio: "))

        num1 = list(map(int,input("\nIngrese los elementos del primer polinomio: ").strip().split(',')))[:num11]
        num2 = list(map(int,input("\nIngrese los elementos del segundo polinomio: ").strip().split(',')))[:num22]

        if opcion == 1:
            calculo.suma(num1,num2)
        elif opcion == 2:
            calculo.resta(num1,num2)
        else:
            print("No es posible realizar la operacion, por favor ingrese una opcion de las disponibles en el menu")