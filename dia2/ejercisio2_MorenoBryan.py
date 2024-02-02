#----jueguito adivina el numero-------
import random

num_intentos = 0
minimo = 1
maximo = 100

# Saludo y solicitud del nombre
print("Hola usuario, ¿cuál es tu nombre?: ")
nombre = input()

# Introducción al juego
print(f"Muy bien, {nombre}, este juego es sencillo.")
print(f"El sistema generará un número aleatorio entre {minimo} y {maximo}.")
print("Tendrás 10 intentos para adivinarlo.")
print("En cada intento fallido se te dará una pista. El juego acabará si se agotan tus intentos o si adivinas el número. ¡Buena suerte!")

# Generar número aleatorio
numero_aleatorio = random.randint(minimo, maximo)

print(f"Ya tengo pensado el número entre {minimo} y {maximo}.")
print(f"Ahora debes adivinarlo, {nombre}.")

# Bucle del juego
while num_intentos < 10:
    try:   
        # entrada del numero del usuario
        print("Ingresa un número: ")
        guess = int(input())
        
        # Incremento del número de intentos
        num_intentos += 1
        
        if guess < numero_aleatorio:
            print("Tu número es demasiado bajo.")
        elif guess > numero_aleatorio:
            print("El número es demasiado alto.")
        else:
            # Si el número es correcto, salir del bucle
            print(f"¡Bien hecho, {nombre}! ¡Has ganado!")
            break

        # Pista sobre el número de intentos
        print(f"Ya llevas {num_intentos} intentos.")

    except ValueError:
        #si se ingresa un valor no válido se va a capturar la exepcion
        print("ERROR: Ingresaste un valor no válido.")

# Mensaje si se agotan los intentos
if num_intentos == 10:
    print(f"Lo siento, {nombre}, has agotado tus 10 intentos. El número correcto era {numero_aleatorio}.")