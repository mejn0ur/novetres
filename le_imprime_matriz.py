#programa recebe numeros de uma matriz e retorna a matriz

print 'Este programa recebe uma matriz e imprime-a.'
print ''

matriz = []
linha = []

print 'Entre com a quantidade de linhas:'
lin = int(raw_input('-> '))

print 'Entre com a quantidade de colunas:'
col = int(raw_input('-> '))

print 'E agora a matriz.'

for i in range (1, lin + 1):
    print 'linha: ', i
    for j in range (1, col + 1):
        print 'Entre com o termo numero: ', j
        num = float(raw_input('-> '))
        linha = linha + [num]
    matriz = matriz + [linha]
    linha = []

print 'Segue matriz.'

for l in matriz:
  print l