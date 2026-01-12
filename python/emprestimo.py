# Solicita os dados ao usuário
valor_casa = float(input("Digite o valor da casa: R$ "))
salario = float(input("Digite o salário do comprador: R$ "))
anos = int(input("Digite em quantos anos deseja pagar: "))

# Calcula a prestação mensal
meses = anos * 12
prestacao = valor_casa / meses

# Calcula o limite permitido (30% do salário)
limite = salario * 0.3

# Verifica se o empréstimo pode ser aprovado
if prestacao <= limite:
    print(f"Empréstimo APROVADO! A prestação será de R$ {prestacao:.2f} por mês durante {meses} meses.")
else:
    print(f"Empréstimo NEGADO! A prestação de R$ {prestacao:.2f} excede 30% do seu salário (R$ {limite:.2f}).")
