print("Hola bienvenido al test sobre que telefono comprar")
print ("_"*52)

Telefono= input("Antes de nada ¿Qué sistema operativo te interesa mas? (Andoid o Ios): ")

if Telefono== "Android":
    print("Entendido, eres usuario de Android")
    Presupuesto= int(input("¿Cual es tu presupuesto en euros?"))
    if Presupuesto <= 400:
        print("Tu telefono ideal es un Xiaomi o un Poco")
    if Presupuesto >=401:
        Especificaciones= input("¿Que es mas importante para ti? Camara, potencia o pantalla: ")
        if Especificaciones== "Camara":
            print ("En ese caso te recomiendo un Google Pixel Supercamera")
        elif Especificaciones== "potencia":
            print ("En ese caso te recomendaria un Oppo Find X3 Pro ")
        elif Especificaciones== "pantalla":
            print("En ese caso deberias escoger un tope de gama de Samsung")
if Telefono== "Ios":
    print("Asi que eres de esos ehh...")
    Presupuesto2=int(input("¿Y cuanto te quieres gastar aprox?"))
    if Presupuesto2 >= 701:
        print("Tu telefono ideal es Iphone13 Pro Max")
    if Presupuesto2 <=700:
       Segundamano= input("¿Te importa que tu telefono sea de segundamano? (Si/NO)")
    if Segundamano== "Si" or "si":
            print ("En ese caso te recomiendo un IphoneSE")
    elif Segundamano== "No" or "no":
            print ("Pues lo ideal seria un Iphone X en adelante")


