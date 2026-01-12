while True:
    num = int(input('Digite um numero:'))

    if num < 0:
        print('Programa encerrado')
        break # Sai do loop se o numero for negativo

    print(f'\nTabuada do {num}:')
    for i in range(1, 11): #Tabuada de 1 a 10
        print(f'{num} x {i} = {num * i}')  
        print('-' * 30)          #Linha separadora
