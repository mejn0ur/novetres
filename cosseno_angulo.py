#Este programa calcula o cosseno de um angulo
#lido atraves do TGT - Teorema Geral da Trigonometria

#Antes de tudo, importamos a biblioteca math

import math

print 'Entre com o angulo cujo cosseno calcularemos:'
angulo = float(raw_input('> '))

print 'O resultado pode obtido de 3 maneiras:'
print ' '
print '1. Calculando (cos(x))^2 = 1 - (sen(x))^2 // com o sen(x) calculado a partir da funcao math.sin()'
print '2. Calculando cos(x) = 1 - sen(x) // com o sen(x) lido, caso seja um angulo conhecido.'
print '3. Usando a funcao math.cos() pura.'

print ' '
print 'O angulo tem seno conhecido? (sim/nao)'
resp = raw_input('> ')

if resp == 'nao':
    print 'Deseja calcular pela funcao math.sin() - 1 - ou pela funcao math.cos() - 2 - ?'
    resp2 = raw_input('> ')

    if resp2 == '1':
        cos = math.sqrt(1 - math.sin(angulo))
        
        print 'O cosseno do angulo dado e: ', cos

    elif resp2 == '2':
        cos = math.cos(angulo)

        print 'O cosseno do angulo dado e: ', cos

elif resp == 'sim':
    print 'Por favor entre com o seno do angulo:'
    sen = float(raw_input('> '))

    cos = math.sqrt(1 - (sen**2))

    print 'O cosseno do angulo dado e: ', cos

print 'Obrigado por usar nosso programa!'