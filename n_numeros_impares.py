#Dado um número inteiro positivo n, 
#imprimir os n primeiros naturais ímpares.

x = int(input('no: '))

y = 1

print('números ímpares: ')

for i in range(x):
	print (y, end=', ')

	y = y + 2