Titulo= " Bienvenido, ¿Cuanto sabes de la Tierra?"
print ("\n"+ Titulo + "\n"+ "_"*27)
Puntuacion=0
opcion= input("¿Cuantos años tiene el planeta? \n"
              "A- 4543,9 millones de años\n"
              "B- 2021 años\n"
              "C- 32,5 millones de años\n"
              "D- 1000000 años\n")
if opcion=="A":
    Puntuacion= Puntuacion + 10
    print("¡Acertaste!")
elif opcion=="B":
    Puntuacion = Puntuacion + 0
    print("¡Has fallado!")
elif opcion == "C":
    Puntuacion = Puntuacion + 0
    print("¡Has fallado!")
elif opcion == "D":
    Puntuacion = Puntuacion + 0
    print("¡Has fallado!")
else:
    print("Esa no era una respuesta válida")
print("Tu puntuación es: {} puntos.".format (Puntuacion))
print("Siguiente pregunta: ")
opcion= input("¿Como se llamaba el supercontinete antes de que se dividiese? \n"
              "A- Nueva York\n"
              "B- Titan\n"
              "C- Pangea\n"
              "D- Olympus\n")
if opcion=="A":
    Puntuacion= Puntuacion + 0
    print("¡Has fallado!")
elif opcion=="B":
    Puntuacion = Puntuacion + 0
    print("¡Has fallado!")
elif opcion == "C":
    Puntuacion = Puntuacion + 10
    print("¡Acertaste!")
elif opcion == "D":
    Puntuacion = Puntuacion + 0
    print("¡Has fallado!")
else:
    print("Esa no era una respuesta válida")
print("Tu puntuación es: {} puntos.".format (Puntuacion))
print("Siguiente pregunta: ")
opcion= input("¿Como se llama la linia imaginaria que divide los husos horarios? \n"
              "A- Translantes\n"
              "B- Linias de Gaus\n"
              "C- Meridianos\n"
              "D- Linias imaginarias\n")
if opcion=="A":
    Puntuacion= Puntuacion + 0
    print("¡Has fallado!")
elif opcion=="B":
    Puntuacion = Puntuacion + 0
    print("¡Has fallado!")
elif opcion == "C":
    Puntuacion = Puntuacion + 10
    print("¡Acertaste!")
elif opcion == "D":
    Puntuacion = Puntuacion + 0
    print("¡Has fallado!")
else:
    print("Esa no era una respuesta válida")
print("Tu puntuación es: {} puntos.".format (Puntuacion))

if Puntuacion <=9:
    print("No tienes ni idea vuelve a la ESO")

elif Puntuacion <=20:
    print("No esta mal pero deberias practicar mas")

elif Puntuacion >=21:
    print("Madremia de locos el bicho de la Geografia")