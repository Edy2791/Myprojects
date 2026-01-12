altura = float(input('Qual e a sua altura?'))
peso = float(input('Qual e o seu peso?'))

imc = peso / (altura **2)

if peso <= 18.5:
    print('Voce esta abaixo do peso')
elif peso >= 18.5 or peso < 25:
    print('Voce esta com um peso ideal')
elif peso >=25 or peso >30:
    print('Sobrepeso')
