print("EJERCICIO 2")
print()
#Los años bisiestos son divisibles entre 4
#No son divisibles entre 100
#Si son divisibles entre 400

anio = int(input("Ingrese el año: "))

if anio % 4 == 0:
    if anio % 100 == 0:
        if anio % 400 == 0:
            print("El año",anio,"es bisiesto")
        else:
            print("El año",anio,"no es bisiesto")
    else:
        print("El año",anio,"es bisiesto")
else:
    print("El año",anio,"es no bisiesto")