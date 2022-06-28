import math
GB = int(input("ingresa los datos:"))
MG = float(1024 * GB)
MD = MG /1.44

print("Numero de Discos necesarios: ", math.ceil(MD)) 


