#Dado um número inteiro positivo n, 
#calcular a soma dos n primeiros números naturais. 

x = int(input('no: '))

y = 0

for i in range(x+1):
	y = y + i

print ('a soma dos n termos é: ', y)