#CONDICIONAL ANIDADA
#Determina la etapa de vida de una persona con base a su edad
#Niñez      0-12
#Adolecencia 13-18
#Adulto    19-59
#Adulto mayor >=60


edad = int(input("Ingresa tu edad: "))

if edad >= 0 and edad <=12:
    print("Etapa niñez")
else:
    if edad >= 13 and edad <=18:
        print("Etapa adolecencia")
    else:
        if edad >=19 and edad <=59:
            print("Etapa adulto")
        else:
            if edad >=60 and edad <=115:
                print("Etapa adulto mayor")
            else:
                print("Edad no válida")