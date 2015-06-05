#programa que ir procurar o maior termo de uma lista

lista = []

print 'Quantos termos tem a lista?'
qtd = int(raw_input('-> '))

print 'Entre com os termos:'

for i in range (1, qtd + 1):
    num = int(raw_input('-> '))
    lista = lista + [num]

maior = 0

for j in lista:
    for k in lista:
        if j > k and j > maior:
            maior = j

print 'O maior e: ', maior