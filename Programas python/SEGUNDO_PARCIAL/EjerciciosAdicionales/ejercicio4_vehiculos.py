#Para calcular el tiempo de encuentro se divide la distancia sobre la suma 
#de las velocidades
print("EJERCICIO 4")
print()

velocidad1 = float(input("Ingresa la velocidad del primer automóvil: "))
velocidad2 = float(input("Ingresa la veocidad del segundo automóvil: "))
distancia = float(input("Ingresa la distancia que los separa: "))

if velocidad1 > 0 and velocidad2 > 0:
    suma = velocidad1 + velocidad2
    TE = distancia / suma
    print("El tiempo de encuentro de los dos vehículos es: ",TE)
else:
    print("Datos erróneos")