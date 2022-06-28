#range() imprimir valores de un rango

#Si range() recibe un parámetro, se interpreta como el número en donde termina el rango-1
for x in range(5):
    print(x)

#Si range() recibe dos parámetros, se interpreta como:
#El primer parámetro es el inicio
#El segundo parámetro es  en donde termina el rango-1
for y in range(1,11):
    print(y)

#Si range() recibe tres parámetros, se interpreta como:
#El primer parámetro es el inicio
#El segundo parámetro es en donde termina el rango-1
#El tercer parámetro es el incremento
for z in range(10,51,5):
    print(z)