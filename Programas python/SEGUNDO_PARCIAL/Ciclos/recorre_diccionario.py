#Diccionario: Es un tipo de colección compuesta por varios elementos que
#poseen Clave-Valor

numeros_telefonicos = {"Contacto 1": 2711873427, "Contacto 2": 27111323427, "Contacto 3": 2711873256}

#items() permite acceder a los valores del dicionario

for clave,valor in numeros_telefonicos.items():
    print("Clave:", clave, "Valor:", valor)
    #print("Clave:" + clave + "Valor:" + str(valor))