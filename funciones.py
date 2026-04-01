# Funciones
""" 
template string => `Hola, ${nombre}`

Javascript:

1. Funciones de Nombre

    function nombreFuncion(params){
        codigo
    }
    
2. Funciones expresivas

    const nombreFuncion = function(params){
        codigo
    }
    
3. Funciones Flecha

    const sumar = (a, b) => a + b


Python:

def nombre_funcion(params):
    codigo
    
sumar = lambda a, b : a + b

"""

def imprimir_nombre(nombre, apellido):
    return f"Hola, {nombre} {apellido}" # Hola, John

print(imprimir_nombre("John", "Doe")) # Hola, John


# 1. Parametros Posicionales
def saludar(nombre, apellido):
    print(f"Hola, {nombre} {apellido} ¿como estas?")

saludar("John", "Doe")

# 2. Parametros por Defecto

def saludar(nombre, apellido = "Doe"):
    print(f"Hola, {nombre} {apellido} ¿como estas?")

saludar("Peter", "Doe")
saludar("Jane")

# 3. Argumentos Nombrados (keyword)
def saludar(nombre, edad, apellido = "Doe"):
    print(f"Hola, {nombre} {apellido} ¿como estas?, tengo {edad} años de edad.")
    
saludar(edad=40, apellido="Rodriguez", nombre="Luis")

# 4. Argumentos Variables (*args)

def totalizar(*numeros):
    return sum(numeros)

print(totalizar(1, 2))
print(totalizar(1, 2, 3, 4))
print(totalizar(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# 5. Argumentos Clave-Valor (**kargs)
def mostrar_datos(**kargs):
    print(kargs)
    print(f"Mi nombre es: {kargs["nombre"]} {kargs["apellido"]}, tengo {kargs["edad"]} años y vivo en {kargs["direccion"]}")
    
mostrar_datos(nombre="Luis", apellido="Rodriguez", edad=44, direccion="Santigo, Chile")