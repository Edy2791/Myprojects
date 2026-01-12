#Variaveis
Idade = int(input('Que idade o Edy tem?'))
bairro = str(input('Em que bairro o Edy nasceu?'))
Edy = str(input('Voce conhece bem o Edy?'))


#Condicoes aninhadas
if Edy == 'Sim':
    print('Esta bem, entao responda as seguintes questoes sobre o Edy')
Questoes = int(input('Quantos irmaos o Edy tem?'))
if Questoes >= 4:
    print('Certo')
elif Questoes > 4 or Questoes < 4:
    print('Errado')

Gostos = str(input('Voce conhece os gostos do Edy?'))

if Gostos == 'Nao':
    print('Opss, que pena!')
else:
    print('Esta bem, vamos a algumas questoes')

Favoritos = str(input('Qual e o desporto que o Edy mais gosta de acompanhar?'))
if Favoritos =='Futebol':
    print('Correcto')
else:
    print('Errado, voce nao conhece bem o Edy!')
print('Parabens Edy, continue praticando mais')