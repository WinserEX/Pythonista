# 1- Escriba en pantalla el tipo de dato que retorna la expresión 4 < 2
print(type(4 > 2))

# 2- Almacene en una variable el nombre de una persona y al final muestre en la consola el mensaje:  “Bienvenido [nombrePersona]”
x = 'Winser'
print("Bienvenido", x)

# 3- Evalúe si un número es par o impar y muestre en la consola el mensaje.
even_Noteven = float(input('Tu número: '))
result = even_Noteven % 2
if result == 0:
    print(round(even_Noteven), "es par")
else:
    print(round(even_Noteven), "es inpar")

# 4- Almacene dos números y evalúe si el primero es mayor que el segundo. El resultado debe verse  en la consola.
first_number = float(input('1er número: '))
second_number = float(input('2do número: '))

if first_number > second_number:
    print(round(first_number),'es mayor a',round(second_number))
elif first_number < second_number:
    print(round(first_number), 'es menor a', round(second_number))
else:
    print(round(first_number), 'es igual a', round(second_number))

# 5- Convierta dólares a pesos.
dolares = float(input('Inserte cantidad de dolares para convertir en pesos: '))
pesos = 56
print('US$', round(dolares), 'son', round(dolares * pesos))

# 6- Convierta grados celsius a Fahrenheit
grados_celcius = float(input('Inserte temperatura en Grados Celcius para convertir a Fahrenheit: '))
print((grados_celcius * 1.8) + 32, 'Fahrenheit')

# 7- Almacene cuatro notas 90,95,77, 92 y las promedio. Al final debe decir su calificación en letras A, B,C,D, E ó F. 
primera_nota = float(input('Inserte 1ra nota: '))
segunda_nota = float(input('Inserte 2da nota: '))
tercera_nota = float(input('Inserte 3ra nota: '))
cuarta_nota = float(input('Inserte 4ta nota: '))

promedio = (primera_nota + segunda_nota + tercera_nota + cuarta_nota)/4

if promedio >= 90:
    print('A')
elif promedio >= 80 and promedio <= 89:
    print('B')
elif promedio >= 70 and promedio <= 79:
    print('C')
elif promedio >= 60 and promedio <= 69:
    print('D')
elif promedio >= 50 and promedio <= 59:
    print('E')
else:
    print('F')

# 8- Que almacene monto, cantidad de cuotas, y porcentaje de interés anual de un préstamo y  calcule la cuota mensual. (Amortizar mediante el sistema francés)
monto = float(input('¿Cuál es el monto del prestamo? '))
cuotas = float(input('¿Cuántas cuotas tiene el prestamo? '))
interes_anual = float(input('¿Cuál es el porcentaje de interés anual del prestamo? '))

cuota_mensual = monto/cuotas
resultado = round(cuota_mensual + ((cuota_mensual*12)*(interes_anual)/12))
print('Su cuota mensual es: ','RD$',resultado)
print('En total usted pagará','RD$',round(resultado*cuotas), 'por su prestamo de', 'RD$',round(monto))







