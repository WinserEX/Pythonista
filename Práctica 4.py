#1- Modele tres entidades del mundo real, colocar por lo menos 3  características distintivas. 
from typing_extensions import Self
from unicodedata import name


class Plato:
  def __init__(self, nombre, origen, sazon):
    self.nombre = nombre
    self.origen = origen
    self.sazon = sazon
  
  
Pla1 = Plato("arroz con habichuelas", "Santo Domingo", "Verduras")

print(f'El {Pla1.nombre} es de {Pla1.origen} y se cocina con {Pla1.sazon}') 


class Historieta:
  def __init__(self, nombre, escritor, lapices, colorista):
    self.nombre = nombre
    self.escritor = escritor
    self.lapices = lapices
    self.colorista = colorista
  
  
Comic1 = Historieta("Duarte como Nunca Antes Visto", "Jorge E. Perez", "Elkys Nova", "Eddaviel")

print(f'{Comic1.nombre} fue escrito por {Comic1.escritor} dibujado por {Comic1.lapices} y coloreado por {Comic1.colorista}') 


class Autor:
  def __init__(self, nombre, apellido, oficio):
    self.nombre = nombre
    self.apellido = apellido
    self.oficio = oficio
 
 
  def klk(self):
    print(f'{self.nombre} {self.apellido} es {self.oficio}')

        
Autor1 = Autor("Jorge E.", "Perez", "Escritor")

Autor1.klk()


#2- Crear una clase llamada Estudiante con un campo llamado promedio, el cual  solo podrá ser accedido mediante un metodo. 
# El valor del promedio no puede  estar por encima de 100 que es la nota máxima. 

class Estudiante:
    def __init__(self, promedio):
        self.promedio = promedio


    def pro(self):
        if(self.promedio > 100):
            print("Promedio incorrecto")
        else:
            print(self.promedio)

estudiante1 = Estudiante(101)

estudiante1.pro()

#3- Hacer una clase llamada Aritmética, que contenga métodos para cada una de  las operaciones aritméticas básicas. 
class Aritmetica:
    def __init__(self, math1, math2):
        self.math1 = math1
        self.math2 = math2
    

    def suma(self):
        print(self.math1 + self.math2)
    

    def resta(self):
        print(self.math1 - self.math2)
    

    def mult(self):
        print(self.math1 * self.math2)
    

    def div(self):
        print(self.math1 / self.math2)


o1 = Aritmetica(5, 5)
o1.suma()
o1.resta()
o1.mult()
o1.div()
    



#4- Cree una clase llamada Personaje con los métodos de instancia MoverArriba,  MoverAbajo, MoverDerecha y MoverIzquierda. 
# Cree una clase llamada Mario y  otra clase llamada Koopa que herede las funcionalidades de la clase Personaje. 
class Personaje:
    def __init__(self):
        pass

    def mover(self, mov):
        if mov == "arriba":
            print(f'{self.name} saltó')
        
        elif mov == "abajo":
            print(f'{self.name} se agachó')
        
        elif mov == "izquierda":
            print(f'{self.name} se movió a la izquierda')
        
        elif mov == "derecha":
            print(f'{self.name} se movió a la derecha')
        
        else:
            print(f'{self.name} no responde a ese comando, mamma mia!')


class Mario(Personaje):
    def __init__(self):
        Personaje().__init__() 
        self.name = "Mario"

class Koopa(Personaje):
    def __init__(self):
        Personaje().__init__() 
        self.name = "Koopa"

p1 = Mario()
p1.mover("arriba")
p2 = Koopa()
p2.mover("izquierda")    
         



#5- Cree una clase Carro, con un campo llamado _cantidadCombustible y un  método que se llame Encender el cual en base a la gasolina disponible
#   mostrara si el carro pudo o no avanzar. Cada vez que el método se ejecute,  deberá restarse 1 a la gasolina disponible. La cantidad de gasolina debe  establecerse al momento de instanciar un objeto de del tipo de la clase.

class Carro:
    def __init__(self):
        self._cantidadCombustible = 12

    def encender(self):
        if self._cantidadCombustible > 0:
            self._cantidadCombustible -= 1
            print(f'¡Broom, broooom! Quedan {self._cantidadCombustible} galones de combustible')
        elif self._cantidadCombustible == 0:
            print("hecha gasolina")


Toyota2014 = Carro()
for x in range(13):
    Toyota2014.encender()