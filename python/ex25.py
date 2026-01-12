lanche = 'Hamburger', 'Suco', 'Pizza', 'Pudim','Batata Frita'
#As tuplas sao imutaveis
for cont in range (0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')

for comida in lanche:
    print(f'Eu vou comer {comida}')

print('Comi pra caramba!')