#Dada uma seqüência de números inteiros 
#não-nulos, seguida por 0, imprimir seus quadrados.

x = int(input("no: "))

while x != 0:
	quad = x ** 2
	print ('o quadrado de ', x, ' é: ', quad)

	x = int(input("no: "))