#este programa recebe um raio qualquer
#e calcula a area e o perimetro de uma circunferencia

import math

print 'Entre com o raio:'
raio = float(raw_input('> '))

area = math.pi * (raio ** 2)
peri = math.pi * 2 * raio

print 'A area da cincunferencia e: ', area, '; e o seu perimetro e: ', peri, '.'
print 'Obrigado por usar nosso programa!'