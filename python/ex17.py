from random import randint
computador = randint(0, 5)# Faz o computador 'pensar'
print('-=-' *20 )
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-' *20)
jogador = int(input('Em que numero eu pensei?')) #Jogador tenta adivinhar
if jogador == computador:
    print('Parabens! Voce conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no numero {} e nao no {}!'.format(computador, jogador))


