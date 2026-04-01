# Ciclos
""" 

Javascript:

for
for in
for of
while
do while

Python:

for in
while


Ejemplo:

for(let i = 1; i <= 10; i++){
    console.log(i)
}

operador (++) no existe dentro de python


"""

for i in range(1, 11): # range(start=0, stop, step=1)
    print(i)
    
nombres = ["Hugo", "Paco", "Luis"]

for indice in range(len(nombres)):
    print(nombres[indice])
    
for nombre in nombres:
    print(nombre)
    

numero = 1
while numero <= 10:
    print(numero)
    numero+=1
    # numero = numero + 1
    
indice = 0
while indice < len(nombres):
    print(nombres[indice])
    indice+=1