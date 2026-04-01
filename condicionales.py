# Condicionales 
""" 
Javascript:

if (condicion) {
    codigo
}

if (condicion) {
    codigo
} else {
    codigo
}

if (condicion) {
    codigo
} else if (condicion) {
    codigo
} else {
    codigo
}

Python:

if condicion:
    codigo
    
if condicion:
    codigo
else:
    codigo

if condicion:
    codigo
elif condicion:
    codigo
else:
    codigo
    
    
Operadores Logicos:

JS: && || !
PY: and or not


Operadores de Comparacion:

==
!=
>=
<=
>
<


"""
a = 10
b = 8
c = 20

if a == b and a == c:
    print("Condiciones Cumplidas")
    
if a == b:
    print("Iguales")
else:
    print("Desiguales")
    
if a > b and a > c:
    print("A")
elif b > c:
    print("B")
else:
    print("C")
    
    
if 5 == '5':
    print("Verdadero")
else:
    print("Falso")