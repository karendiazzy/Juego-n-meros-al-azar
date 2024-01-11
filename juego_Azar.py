from random import *
numeros= range(0,100)
aleatorio= choice(numeros)

nombre = str(input("Hola, paara empezar ingresa aqui tu nombre:  "))

for num in range(3):
    num= int(input("He pensado en un numero del 1 al 100, Tienes 8 intentos ¿Cual  crees tu que es?:  "))
    
    if num < 1:
        print(f"{nombre} No esta permitido ese valor")
    elif num > 100:
        print(f"{nombre}No esta permitido ese valor")
    elif num < aleatorio:
        print(f"{nombre} El numero que ingreso es menor al correcto")
    elif num > aleatorio:
         print(f"{nombre} El numero que ingreso es mayor al correcto")
    elif num == aleatorio:
        print(f"{nombre}El numero que ingreso es correcto! HAZ GANADO EL JUEGO")
        break
print(aleatorio)