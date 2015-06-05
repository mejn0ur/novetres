#Dados um inteiro x e um inteiro não-negativo n,
#calcular x elevado a n sem uso do sinal **

x = int(input('no x: '))
n = int(input('no n: '))
quad = 1

for i in range(n):
	quad = quad * x

print ('a potencia de', x, ' elevado a ', n, ', é: ', quad)