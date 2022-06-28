print("EJERCICIO 1")
print()

sueldo = float(input("Ingrese el sueldo: "))

if sueldo < 1000:
    aumento = sueldo * (.15)
    suma = sueldo + aumento
    print("Su sueldo es de ", sueldo,"mas los", aumento, " del aumento usted ganará", suma)
else:
    print("No tiene aumento: ", sueldo)