from math import radians, sin, cos, tan
angulo = float(input('Digite o angulo que voce deseja:'))
seno = sin(radians(angulo))
print('O angulo de {} tem o SENO de {}'.format(angulo, seno))
cosseno= cos(radians(angulo))
print('O angulo  de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O angulo de {} tem tangente de {:.2f}'.format(angulo, tangente))