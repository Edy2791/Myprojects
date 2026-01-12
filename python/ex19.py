distancia = float(input('Qual e a distancia da sua viagem?'))
print('Voce esta prestes a comecar uma viagem de {}km.'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('E o preco da sua passagem sera de MT {}'.format(preco))