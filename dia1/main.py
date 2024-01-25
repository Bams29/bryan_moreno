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
##deployed by Bryan Alexander Moreno Sarmiento

