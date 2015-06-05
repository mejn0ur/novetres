#programa recebe duas matrizes e soma-as

print 'Entre com a qtd de linhas das matrizes:'
l = int(raw_input('-> '))

print 'Entre com a qtd de colunas das matrizes:'
c = int(raw_input('-> '))

print 'Entre com a primeira matriz:'

linha = []
matriz1 = []
matriz2 = []
matriz = []

for i in range (1, l + 1):
    print 'Linha: ', i
    for j in range (1, c + 1):
        print 'Coluna: ', j
        num = float(raw_input('-> '))
        linha = linha + [num]
    matriz1 = matriz1 + [linha]
    linha = []

print 'Entre com a segunda matriz:'

for k in range (1, l + 1):
    print 'Coluna: ', k
    for l in range (1, c + 1):
        print 'Linha: ', l
        num = float(raw_input('-> '))
        linha = linha + [num]
    matriz2 = matriz2 + [linha]
    linha = []

print 'Matriz 1:'

for i in matriz1:
    print i

print 'Matriz 2:'

for i in matriz2:
    print i

for i in range(len(matriz1)):
    aux = []
    for j in range(len(matriz1[i])):
        aux += [matriz1[i][j]+matriz2[i][j]]
    matriz += [aux]

print 'Resultado:'
for i in matriz:
    print i