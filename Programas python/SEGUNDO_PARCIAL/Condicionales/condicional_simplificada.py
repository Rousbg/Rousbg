#CONDICIONAL ANIDADA SIMPLIFICADA
edad = int(input("Ingresa tu edad: "))

if edad >= 0 and edad <= 12:
    print("Etapa niñez")
elif edad >= 13 and edad <=18:
    print("Etapa adolecencia")
elif edad >=19 and edad <=59:
    print("Etapa adulto")
elif edad >=60 and edad <=115:
    print("Etapa adulto mayor")
else:
    print("Edad no válida")