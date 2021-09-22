edad= int(input("Indica tu edad: "))
carnet = input("Indica el tipo de carnet (E  Estudiante / P Pensionista / F Failia numerosa/ N Nada):  ")
if (edad <= 35 and edad >= 25 and carnet== "E") or edad <= 10 or (edad >= 65 and carnet== "P") or carnet== "F":
    print("Se te aplica el descuento")
else:
    print("No se te aplica el descuento")