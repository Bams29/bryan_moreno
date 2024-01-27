#-----Ecuacion fibonacci--------
#ejercisio#1_MorenoBryan.py
#saludo y explicacion sobre la serie de fibonacci
print("hola usuario")
print("        ")
print("te dare una pequeña explicacion sobre la serie de fibinaccci antes de empezar")
print("Se trata de una secuencia infinita de números naturales; ")
print("a partir del 0 y el 1, se van sumando a pares, de manera que cada número es igual a la suma de sus dos anteriores")

#entrada del numero hasta donde se dara la serie
def pideNumero():
    while True:
        try:
            n = int(input("ingresa un numero mayor a 1 (0 si gusta salir): "))
            if n == 0:
                print("gracias por usar este codigo, ciao")
                exit()
            if n>1:
                return n
            else:
                print("elige un numero positivo mayor a 1")
        except ValueError:
            print("ERROR: eligio un valor inadecuado")
#generacion de la lista donde se mostrara la serie
def generafib(n):
    lista=[]
    for i in range(0,n):
        if i == 0 or i==1:
            lista.append(1)
        else:
            lista.append(lista[i-2]+lista[i-1])
            
    return lista
#generacion de la lista junto a la serie
def muestraLista(lista):
    for i in lista:
        if(i!=lista[-1]):
            print(f"{i}", end="+")
        else:
            print(f"{i}")

n=pideNumero()
lista=generafib(n)
muestraLista(lista)