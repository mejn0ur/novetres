#Dados o número n de alunos de uma turma 
#e suas notas da primeira prova, 
#determinar a maior e a menor nota obtidas 
#por essa turma (Nota máxima = 100 e nota 
#mínima = 0). 

n = int(input('Entre com o numero de alunos: '))

nmax = 0
nmin = 100

for i in range(1,n+1):

	nota = int(input('Nota %i: ' % i))

	if nota > nmax:
		nmax = nota
	if nota < nmin:
		nmin = nota

print ('A maior nota é %i e a menor é %i' %(nmax, nmin))