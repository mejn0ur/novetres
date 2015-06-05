#Este programa calcula o indice de massa
#corporea de uma pessoa.

#O IMC e calculado apartir de uma relacao IMC = Peso / Altura^2

print 'Entre com o seu peso:'
peso = float(raw_input('> '))

print 'Entre com a sua altura:'
altura = float(raw_input('> '))

#Segue calculo

imc = peso / (altura * altura)

print 'Seu Indice de Massa Corporea e de:', imc

if imc <= 18.5:
    print 'Voce esta abaixo do peso ideal'

elif imc > 18.5 and imc <= 24.9:
    print 'Parabens! Voce esta no peso ideal'

elif imc > 24.9 and imc <= 29.9:
    print 'Voce esta acima do seu peso ideal'

elif imc > 29.9 and imc <= 34.9:
    print 'Obesidade grau I'

elif imc > 34.9 and imc <= 39.9:
    print 'Obesidade grau II'

else:
    print 'Obesidade grau III'


print 'Obrigado por usar este programa!'