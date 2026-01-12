frase = str(input('Digite uma frase: '))
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A letra A aparece na posicao {} na frase'.format(frase.find('A'))+1)
print('Ela aparece na posicao {} na frase'.format(frase.rfind('A'))+1)
