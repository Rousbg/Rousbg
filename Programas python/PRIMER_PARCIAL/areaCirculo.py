import math #Proporciona acceso a las funciones matemáticas
print("Tarea: Área de un circulo:")
print()
print("Ingrese el radio:")
print()

radio = float(input("radio = " ))
area = math.pi * (radio * radio)

print("Resultado:")
print("El área del circulo es:",round(area, 2))