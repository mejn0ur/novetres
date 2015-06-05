#programa recebe duas matrizes e calcula seu produto

linha = []

print 'Entre com a qtd de linhas da matriz 1:'
l1 = int(raw_input('-> '))

print 'Entre com a qtd de colunas da matriz 1:'
c1 = int(raw_input('-> '))

print 'Leitura da matriz 1:'

matriz1 = []

for i in range (1, l1 + 1):
    print 'Linha: ', i
    for j in range (1, c1 + 1):
        print 'Coluna: ', j
        num = float(raw_input('-> '))
        linha = linha + [num]
    matriz1 = matriz1 + [linha]
    linha = []

print 'Entre com a qtd de linhas da matriz 2:'
l2 = int(raw_input('-> '))

print 'Entre com a qtd de colunas da matriz 2:'
c2 = int(raw_input('-> '))

print 'Leitura da matriz 2:'

matriz2 = []

for i in range (1, l2 + 1):
    print 'Linha: ', i
    for j in range (1, c2 + 1):
        print 'Coluna: ', j
        num = float(raw_input('-> '))
        linha = linha + [num]
    matriz2 = matriz2 + [linha]
    linha = []

print 'Matriz 1:'

for i in matriz1:
    print i

print 'Matriz 2:'

for j in matriz2:
    print j

matriz = []
for i in range(l1):
    maux = []
    for j in range(c2):
        aux = 0.0
        for x in range(c1):
            print i, j, x
            aux += matriz1[i][x] * matriz2[x][j]
        maux += [aux]
    matriz += [maux]

print 'Resultado:'

for i in matriz:
    print i