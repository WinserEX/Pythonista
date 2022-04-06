#1-Realizar un programa que solicite al usuario un número indeterminado de
# números (mientras se tecleen números que no sean cero). Al salir el programa
# debe dar en pantalla el total de números dados y la suma de ellos.

resul = 0
num = ''
num_list = []
while num != 0:
    num = float(input('Agrega todos los números que quieras '))
    num_list.append(round(num))
    resul += num
str_num_list = ",".join([str(x) for x in num_list])

print(f'Luego de introducir {len(num_list)} números, la suma de todos estos es {round(resul)} y los numeros introducidos fueron {str_num_list}')

#2- Realizar un programa que presente un menú con las siguientes opciones
#Convertir grados a Celsius a Fahrenheit
#Convertir dólar a pesos
#Convertir metros a pies
#Salir 
#Cada vez que finalice una de estas acciones debe regresar al menú. 
#El programa solo finalizará cuando el usuario elija la opción salir.

def Celcius_a_F(c):
    return c * 1.8


def Dollar_a_P(p):
    return p / 55


def Metros_a_P(m):
    return m * 3.28


def menu():
    ing = input(
        "Introduzca el # de la opción que necesite: \n 1-Convertir grados Celsius a Fahrenheit \n 2-Convertir dólar a pesos \n 3-Convertir metros a pies \n 4-Salir \n\n")
    if ing == "1":
        grad = int(input("Introduzca Grados Celcius "))
        print(Celcius_a_F(grad))
        return menu()


    elif ing == "2":
        grad = int(input("Introduzca Pesos a convertir "))
        print(Dollar_a_P(grad))
        return menu()

    elif ing == "3":
        grad = int(input("Introduzca Metros a convertir "))
        print(Metros_a_P(grad))
        return menu()

    else:
        print("Gracias por utilizar nuestros servicios")


menu()

# 3- Hacer un programa que genere las tablas de multiplicar de los números
# múltiplos de 5 que hay entre 1 y 1000
def buscar_tablas(num, multiplos):
	i = 1
	while i <= num:
		print(f'{i} x {multiplos} = {i*multiplos}')
		i += 1

buscar_tablas(1000, 5)


# 4 -Realizar un programa que reciba por teclado el sueldo de un empleado y le
# aplique los cálculos de ISR (ver tabla DGII), ARS, y AFP (investigar porcentajes)

def SFS(x):
    SFSa = x * 0.304
    if float(SFSa) >= 4742.40:
        return(4742.40)
    else:
        return(float(SFSa))

def AFP(x):
    AFPa = x * 0.287
    if float(AFPa) >= 8954.40:
        return(8954.40)
    else:
        return(float(AFPa))


def ISR(x,y,z):
    ISRa = x - (y + z)
    ISRb = float(ISRa) * 12
    if ISRb <= 416220:
        resultado = round(ISRa)
        print(f'Tu sueldo está exento de ISR, pero luego de deducir AFP y SFS tu sueldo es {resultado}')
    elif ISRb > 416220 and ISRb <= 624329:
        resultado = round((ISRb - ((ISRb - 416220.01) * 0.15))/12)
        print(f'Tu sueldo menos deducciones es {resultado}')
        print("tier 2")
    elif ISRb > 624329 and ISRb <= 867123:
        resultado = round((ISRb - (31216 + (ISRb - 624329.01) * 0.20))/12)
        print(f'Tu sueldo menos deducciones es {resultado}')
        print("tier 3")
    elif ISRb > 867123:
        resultado = round((ISRb - (31216 + (ISRb - 624329.01) * 0.20))/12)
        print(f'Tu sueldo menos deducciones es {resultado}')
        print("tier 4")
    else:
        print("Datos incorrectos, intentelo de nuevo")
        sueldo = float(input("Introduce tu salario para calcular deducciones "))
        ISR(float(sueldo), float(AFP(sueldo)), float(SFS(sueldo)))


sueldo = float(input("Introduce tu salario para calcular deducciones "))
ISR(float(sueldo),float(AFP(sueldo)),float(SFS(sueldo)))


#5-Cree una aplicación de cajero automático para el banco ABC. El cajero tendrá un  límite de billetes descrito a continuación: 9 de 1000, 19 de 500, 99 de 100 
#El cajero debe solicitar Banco y monto a retirar. Si el banco es ABC el limite de  retiro son 10,000 y 2000 pesos por transacción en caso contrario. 
#El cajero debe informar si el monto solicitado no puede ser dispensado o si  excede el límite de transacción. Y debe hacer la distribución de los billetes de  acuerdo al monto. Por ejemplo, si el usuario solicita 3,900 y hay disponibilidad en todos los billetes, el cajero debe dispensar 3 billetes de mil, 1 de quinientos y 4 de cien.

banco = input("Bienvenido al banco ABC \n ¿Cuál es su banco? \n 1-ABC \n 2-Otro Banco \n")
if banco == "1":
    retiro = int(input("Su límite de retiro es RD$10,000.00 \n ¿cuánto dinero desea retirar? "))
    if retiro > 10000:
        print(f'Su límite de retiro es RD$10,000.00')
    elif retiro <= 10000:
        print(f'Usted retiró {retiro}')
elif banco == "2":
    retiro = int(input("Su límite de retiro es RD$2,000.00 \n ¿cuánto dinero desea retirar? "))
    if retiro > 2000:
        print(f'Su límite de retiro es RD$2,000.00')
    elif retiro <= 2000:
        print(f'Usted retiró {retiro}, si se hace cliente de Banco ABC podrá retirar más')

else:
    retiro = print("Lo sentimos, dato incorrecto")




