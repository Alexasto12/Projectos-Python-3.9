
dolar_euro= 0.85
libra_euro= 1.17
pesoMX_euro=0.043
yuan_euro=0.13
yen_euro=0.0077

print("¡Bienvenido al conversor de divisas!")
print("_"*36)
Moneda= input("¿Que moneda desea convertir?")

if Moneda == "Dolar":
    Cantidad2=float(input("Intorudzca la cantidad en Dolares: "))
    Conversion2= Cantidad2*dolar_euro
    print("{} Dolares Estadounideses son: {} euros.".format (Cantidad2,Conversion2))
elif Moneda == "Dollar":
    Cantidad2=float(input("Intorudzca la cantidad en Dolares: "))
    Conversion2= Cantidad2*dolar_euro
    print("{} Dolares Estadounideses son: {} euros.".format (Cantidad2,Conversion2))
elif Moneda == "dolar":
    Cantidad2=float(input("Intorudzca la cantidad en Dolares: "))
    Conversion2= Cantidad2*dolar_euro
    print("{} Dolares Estadounideses son: {} euros.".format (Cantidad2,Conversion2))
elif Moneda == "dollar":
    Cantidad2=float(input("Intorudzca la cantidad en Dolares: "))
    Conversion2= Cantidad2*dolar_euro
    print("{} Dolares Estadounideses son: {} euros.".format (Cantidad2,Conversion2))
elif Moneda =="Libras":
    Cantidad=float(input("Intorudzca la cantidad en Libras: "))
    Conversion= Cantidad*libra_euro
    print("{} Libras son: {} euros.".format(Cantidad,Conversion))
elif Moneda == "libras":
    Cantidad = float(input("Intorudzca la cantidad en Libras: "))
    Conversion = Cantidad * libra_euro
    print("{} Libras son: {} euros.".format(Cantidad, Conversion))
elif Moneda == "Pesos":
    Cantidad = float(input("Intorudzca la cantidad en Pesos Mexicanos: "))
    Conversion = Cantidad * pesoMX_euro
    print("{} Pesos son: {} euros.".format(Cantidad, Conversion))
elif Moneda == "pesos":
    Cantidad = float(input("Intorudzca la cantidad en Pesos Mexicanos: "))
    Conversion = Cantidad * pesoMX_euro
    print("{} Pesos son: {} euros.".format(Cantidad, Conversion))
elif Moneda == "yuan":
    Cantidad = float(input("Intorudzca la cantidad en Yuanes: "))
    Conversion = Cantidad * yuan_euro
    print("{} Yuanes son: {} euros.".format(Cantidad, Conversion))
elif Moneda == "Yuan":
    Cantidad = float(input("Intorudzca la cantidad en Yuanes: "))
    Conversion = Cantidad * yuan_euro
    print("{} Yuanes son: {} euros.".format(Cantidad, Conversion))
elif Moneda == "Yen":
    Cantidad = float(input("Intorudzca la cantidad en Yenes: "))
    Conversion = Cantidad * yen_euro
    print("{} Yenes son: {} euros.".format(Cantidad, Conversion))
elif Moneda == "yen":
    Cantidad = float(input("Intorudzca la cantidad en Yenes: "))
    Conversion = Cantidad * yen_euro
    print("{} Yenes son: {} euros.".format(Cantidad, Conversion))
else:
    print("¿Que moneda es esa?")
print("_"*36)
