print("Voy a la cocina")
print("Abro la nevera")
hay_leche= input("¿Hay leche? (S/N) ")
hay_Colacao=input("¿Hay Colacao(S/N)")

if hay_leche!= "S" or hay_Colacao!="S":
    print("Voy al super a comprar ")
    if hay_leche!= "S":
        print("Compro leche")
        print("Te sirves en un vaso")
    if hay_Colacao!= "S":
        print("Compro Colacao")
        hay_Colacao="S"
if hay_leche== "S":
    print ("Te sirves la leche en un vaso")
if hay_Colacao== "S":
    print("Abres el Colacao y te pones 3 cucharadas")

    
