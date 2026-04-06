# OOP - Oriented Object Programming - Programacion Orientada a Objetos
""" 
    Clases -> Plantillas
    Objectos -> Instancias de clases (Plantillas)
"""
# Clase (Plantilla)
class Persona:
    pass

# Objeto (Instancia)
persona1 = Persona()

# Ejemplo Completo
# Clase (Plantilla)
class Persona:
    def __init__(self, nombre = "John", apellido = "Doe"):
        self.nombre = nombre # atributo
        self.apellido = apellido # atributo
        
    def saludar(self): # método
        print(f"Hola, soy {self.nombre} {self.apellido}")
        
# Objeto (Instancia)
persona1 = Persona()
# Acceder al metodo saludar
persona1.saludar()

persona2 = Persona("Jane", "Doe")
persona2.saludar()

persona3 = Persona("Luis", "Rodriguez")
persona3.saludar()


""" 
Conceptos Claves de la OOP
"""

# 1. Encapsulamiento

class Cuenta:
    def __init__(self, saldo = 0):
        self.saldo = saldo
        
    def depositar(self, monto):
        self.saldo += monto
        
    def retirar(self, monto):
        self.saldo -= monto
        
# 2. Abstraccion

class Auto:
    
    def encender(self):
        print("Auto encendido...")
        
auto = Auto()
auto.encender()

# 3. Herencia

class Animal:
    def hablar(self):
        print("Hacer un ruido!")
    
class Perro(Animal):
    def hablar(self):
        print("Ladrar")
    
class Gato(Animal):
    def hablar(self):
        print("Maullar")

animal1 = Animal()
animal2 = Perro()
animal3 = Gato()

animal1.hablar()
animal2.hablar()
animal3.hablar()

# 4 Polimorfismo
animales = [Perro(), Gato()]

for animal in animales:
    animal.hablar()
    
    
# Atributos Privados (Convencion)

class Usuario:
    def __init__(self):
        self.nombre = "John" # publico
        self._apellido = "Doe" # protegido
        self.__rut = "123456" # privado
        
u = Usuario()
u.nombre

class Conductor(Usuario):
    
    def set(self, rut):
        self.__rut = rut
        
    def get(self):
        return self.__rut

conductor = Conductor()
conductor.nombre = "Pedro"
conductor._apellido = "Perez"
conductor.__rut = "123456"

print(conductor.nombre)
print(conductor._apellido)
print(conductor.__rut)

""" 
Público: Accesible desde cualquier lugar.
Protegido (_nombre): Convención para indicar que el atributo/método debe usarse solo internamente o por subclases.
Privado (__nombre): Python aplica name mangling (cambio de nombre) para dificultar el acceso externo, protegiendo los datos.
Getters y Setters: Métodos @property utilizados para obtener o modificar atributos privados de manera controlada
"""

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular # Público
        self.__saldo = saldo # Privado
        
    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            
    @property
    def saldo(self):
        return self.__saldo
    
    
cuenta1 = CuentaBancaria("Enzo", 1000)
cuenta2 = CuentaBancaria("Isabella", 10000)

cuenta1.depositar(1000)
cuenta1.depositar(4500)

cuenta2.depositar(1200)

print(cuenta1.saldo) # Acceso controlado: 6500
print(cuenta2.saldo) # Acceso controlado: 11200

print(cuenta2.__saldo) # AttributeError