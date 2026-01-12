nome = str(input('Digite seu nome completo: '))
print('Muito prazer em te conhecer!', nome)
print('Seu primeiro nome e {}'.format(nome.split()[0]))
print('Seu ultimo nome e {}'.format(nome.split()[-1]))