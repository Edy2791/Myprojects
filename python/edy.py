nome = str(input('Qual e o seu nome?'))
if nome == 'Edy':
    print('Que nome bonito!')
elif nome =='Pedro' or nome =='Adila' or nome =='Paulo':
    print('Seu nome e bem popular em Brasil.')
else:
    print('Seu nome e bem normal.')
print('Tenha um bom dia {}!'.format(nome))