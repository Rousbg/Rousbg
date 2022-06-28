RC = int(input("ingrese cantidad de respuestas correctas:"))
PRC = (RC * 3) 
print("el puntaje es:", PRC)

RI = int(input("ingrese cantidad de respuestas incorrectas:"))
PRI = RI - RI
print("el puntaje es:", PRI)

RB = int(input("ingrese cantidad de respuestas en blanco:"))
PRB = RB * 0
print("el puntaje es:", PRB)

reultadoFinal = PRC + PRI + PRB

print("Resultado final: ", reultadoFinal)