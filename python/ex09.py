nome = str(input('Digite seu nome completo:')).strip()
print('Analisando seu nome...')
print('Seu nome em letras maiusculas e', nome.upper())
print('Seu nome em letras minusculas e', nome.lower())
print('Seu nome tem letras', len(nome) - nome.count(' '))
print('Seu primeiro nome tem letras', nome.find(' '))



