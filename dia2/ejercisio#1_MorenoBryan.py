#-----Ecuacion fibonacci--------

x = 0
y = 1
z = 0

print ("bienvenido usuario, entes de que inicies se te dara una breve explicacion sobre lo que es la seire de fibonacci.")
print("  ")
print ("esta msima Se trata de una secuencia infinita de números naturales; a partir del 0 y el 1, se van sumando a pares, de manera que cada número es igual a la suma de sus dos anteriores.")
while True:
    n =int(input("hola usuario, ingresa porfavor un numero ENTERO mayor a 1: "))
    if n>1:
        break
print("1",end=(" "))

for o in range(0, n):
    z = x+y
    print(f"{z}", end=(" "))
    x=y
    y=z
    print("")