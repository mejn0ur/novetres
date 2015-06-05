#este programa le numeros positivos e calcula quais sao primos

lista = []
lista2 = []
cont = 0

print 'Quantos elementos tem a lista?'
qtd = int(raw_input('-> '))

print 'Entre com os ', qtd, 'elementos.'

for i in range(1, qtd + 1):
    num = int(raw_input('-> '))
    lista = lista + [num]

for j in lista:
    for k in range(1, j + 1):
        rst = j % k

        if rst == 0:
            cont = cont + 1

    if cont == 2:
        lista2 = lista2 + [j]

    cont = 0

print 'Os termos primos da lista sao:', lista2