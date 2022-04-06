# 1- Hacer una función que potencie un número x a la y 
def potencia(x,y):
    return x**y


potencia(4,2)


# 2- Realizar una función que pida por pantalla un número del 1 al 10 y muestre  por pantalla el número escrito en letras.

import os
from re import X
def letras(num):
    if num > 0 and num <= 10: 
        def prueba(a):
            if a == 1:
                print("Uno")
            elif a == 2:
                print("Dos")
            elif a == 3:
                print("Tres")
            elif a == 4:
                print("Cuatro")
            elif a == 5:
                print("Cinco")
            elif a == 6:
                print("Seis")
            elif a == 7:
                print("Siete")
            elif a == 8:
                print("Ocho")
            elif a == 9:
                print("Nueve")
            elif a == 10:
                print("Diez")
        os.system("cls")        
        prueba(num)  
        
    else:
        os.system("cls")
        print("Incorrecto, ntroduzca un número del 1 al 10: ")                 
        
while True:
    letras(int(input("Introduzca un número del 1 al 10: ")))

# 3- Hacer una función que reciba un año como argumento y retorne  verdadero si es bisiesto. 
def bisiesto(año):    
  if((año % 400 == 0) or  
     (año % 100 != 0) and  
     (año % 4 == 0)):   
    print("Es bisiesto");  
  else:  
    print("No es bisiesto")    
bisiesto(int(input("Escriba el año para verificar si es bisiesto: ")))  
 
# 4- Crear una función que evalúe dos números y retorne verdadero si ambos  números son iguales. 
def igualdad(x,y):
    if x/y == 1:
        print("Son iguales")
    else:
        print("No son iguales")
while True:
    igualdad(int(input("Introduzca el 1er número: ")),int(input("Introduzca el 2do valor: ")))
    

# 5- Un número palindrómico se lee igual en ambos sentidos. El palíndromo más  grande hecho del producto de dos números de 2 dígitos es 9009 = 91 × 99.  Cree una función que encuentre el palíndromo más grande hecho del  producto de dos números de 3 dígitos. 
def polindro(num):
    x = num
    y = 0
    while(num > 0):
        z = num % 10
        y = y * 10 + z
        num = num // 10
    if(x == y):
        return True
    else:
        return False

def max_poli():
    for i in range(100, 1000):
        r = i * i
        if polindro(r) == True:
            print(f'{i} x {i} = {i * i}')


max_poli()


# 6- Hacer una función que reciba una cedula como argumento y diga si la  cedula es válida o no. 
def id(x):
    if(len(x) != 11):
        print("Su número de cédula no es válido")
    else:
        print(f'Su número de cédula {x} es válido')


id(input("Introduzca su número de cédula sin guiones: "))

# 7- Hacer una función que reciba como argumento una lista de elementos  numéricos y retorno otra lista con cada elemento de la primera lista  duplicados. 
def multi_list():
    str_list = []
    num = input('Ingresa una lista de número separados por comas: ')
    str_list.append(num)
    int_list = [int(x) for x in str_list]    
    print(int_list)


multi_list()

# 8- Hacer una función que reciba un valor inicial y uno final, y muestre en  pantalla las tablas de multiplicar de los números múltiplos de 6 que hay  entre el valor inicial y el valor final.
def seis(y,z):
    for x in range(y,z):
        if x % 6 == 0:
            print(f'{1} x {x} = {1 * x}')
            print(f'{2} x {x} = {2 * x}')
            print(f'{3} x {x} = {3 * x}')
            print(f'{4} x {x} = {4 * x}')
            print(f'{5} x {x} = {5 * x}')
            print(f'{6} x {x} = {6 * x}')
            print(f'{7} x {x} = {7 * x}')
            print(f'{8} x {x} = {8 * x}')
            print(f'{9} x {x} = {9 * x}')
            print(f'{10} x {x} = {10 * x}')
            print(f'{11} x {x} = {11 * x}')
            print(f'{12} x {x} = {12 * x}')


seis(int(input('Introduzca valor incial')),int(input('Introduzca valor final')))