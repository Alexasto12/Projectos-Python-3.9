import random
print("Hola bienvenido a ¡Adivina mi numero!")
print("Solo tienes que escribir un numero del 1 al 10 para ver si lo adivinas. ¿Seras capaz?")
Numero_Ganador=random.randint(0,10)
Numero_Secreto= int(input("Porfavor, escribe tu numero del 0 al 10: "))
if Numero_Secreto > 10:
    print("No te flipes tiene que ser menor a 10")
if Numero_Secreto < 0:
    print ("¡Te has quedado corto! Tiene que ser mayor a 0")
if Numero_Secreto!=Numero_Ganador:
    print("¡Has fallado! El numero ganador era: {}".format(Numero_Ganador))
if Numero_Secreto==Numero_Ganador:
    print ("¡Enhorabuena has acertado!")


