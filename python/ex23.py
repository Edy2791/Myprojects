m = 0
th = 0
tm = 0

while True:
    idade = int(input('Digite a idade:'))
    sexo = ''
    while sexo not in 'MF':
        sexo = input('Digite o sexo [M/F]: ').strip().upper()

        if idade > 18:
            m += 1
        
        if sexo == 'M':
            th += 1