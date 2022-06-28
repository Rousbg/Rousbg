#import math
print("Distancia entre dos puntos")
print()

XA = float(input("Coordenada X de A: "))

YA = float(input("Coordenada Y de A: "))

XB = float(input("Coordenada X de B: "))

YB = float(input("Coordenada Y de B: "))

D  = float(((((XA - XB)**2) +((YA - YB)**2)  )**.5))
print()

print ("Distancia entre el punto A y B : ", round(D,2))