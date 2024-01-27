##---------------------------------------
##------------ejercisio 1------------
##---------------------------------------

#impresion en consola
print ("hola mundo")

#-----Datos primitivos------
# 1. string
texto = "campu"
type(texto)
print (texto)
# 2. int
numero1 = 1
print(numero1)
# 3. float
numerod = 2.33
print(numerod)
# 4. double
numerodecimallargo = 3.56565656567643
print(numerodecimallargo)
# 5. boolean
bool=True
print(bool)
#-----Entradas por parte de usuario------
entradausuario = input("ingresa tu nombre ")
print ("tunombre es: ", entradausuario)
#-----Entradas por parte de usuario con definicion de dato primitivo------
entradausuarioNum= int(input("ingresa your edad: "))
print ("tu edad es: ", entradausuario)

#------Ciclos------
#ciclo for
for i in range(5,10,2):#for N in range(desde,hasta,pasos):
    print(i)
#ciclo while
booli = True
while booli == True: #while condicio cumplir
    print("no eh morio")
    booli = False

##--------Condicionales--------
texto1 = "campus"
if texto == "campus":
    print("yo soy campus")    
else:
    print("mentira no lo soy")

##-----FUNCIONES-------
    
#---funcion sin parametros ni retornos---
def dinumero():
    print("el 3")

dinumero() # llama la funcion de "di numero"

#----funcion con parametros sin retorno----
def HolaConName(name):
    print("Jello "+ name + "!")

HolaConName("federico")#llama la funcion "holaConName", añadiendole el parametro "federico"

#----funciones con parametros y retornos----
def multiplica(val1, val2):
    return val1 * val2

print(multiplica(3, 5))#retorna la multiplicacion de los parametros guardados en la funcion "multiplica"

#-----funciones sin parametro y con retorno-----
def dijelou():
    return print("howdy")

print(dijelou())

##-----DIMENSIONES-------
mi_lista = ["manolo", "joaquin", "marimar", "rosario", "Danna garcia"]
print(mi_lista[0]) # Muestra Juan (la primera posición es la 0)
print(mi_lista[-1]) # Muestra Susana
print(mi_lista[1]) # Muestra Pedro
print(mi_lista[2]) # Muestra Laura
print(mi_lista[-2]) # Muestra Carmen



##deployed by Bryan Alexander Moreno Sarmiento

