#Uma loja de discos anota diariamente durante 
#o mes de marco a quantidade de discos vendidos.
#Determinar em que dia desse mes ocorreu a maior 
#venda e qual foi a quantidade de discos vendida 
#nesse dia.

dia = int(input('Dia: '))
qtd = float(input('Qtd: '))

qtdm = 0

while 1:
	if qtd > qtdm:
		qtdm = qtd
		diam = dia
	elif dia > 3:
		break

	dia = int(input('Dia: '))
	qtd = float(input('Qtd: '))

print ('No dia %i, vendemos %f' % (diam, qtdm))