#programa que recebe uma lista de nomes e testa qual eh o maior nome

lista = []

print 'Quantas palavras tera a lista?'
qtd = int(raw_input('-> '))

for i in range (1, qtd + 1):
    pal = str(raw_input('-> '))
    lista = lista + [pal]

maior = ''

for j in lista:
    for k in lista:
        if len(j) > len(k) and len(j) > len(maior):
            maior = [j]

print 'A maior palavra e: ', maior