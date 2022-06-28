print("Número enteros")
numDecimal1 = 4
numDecimal2 = 3
sumaDecimal = numDecimal1 + numDecimal2
print ("La suma decimal de {} + {} es: {}".format (numDecimal1, numDecimal2, sumaDecimal))

numHexadecimal1 = 0x3FC
numHexadecimal2 = 0x1F68
sumaHexadecimal  = numHexadecimal1 + numHexadecimal2
print ("La suma hexadecimal de {} + {} es : {}".format(oct(numHexadecimal1), hex(numHexadecimal2), hex(sumaHexadecimal)))

numOctal1 = 0o10243
numOctal2 = 0o1703
sumaOctal = numOctal1 + numOctal2
print ("La suma octal de {} + {} es : {}".format(oct(numOctal1), oct(numOctal2), oct(sumaOctal)))