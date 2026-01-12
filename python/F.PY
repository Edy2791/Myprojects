#codigo simples
import math

numero = int(input("Digite um número: "))
print(f"O fatorial de {numero} é {math.factorial(numero)}")


#Uso de loops
def calcular_fatorial(n):
    if n < 0:
        return "Não existe fatorial de número negativo."
    elif n == 0 or n == 1:
        return 1
    else:
        fatorial = 1
        for i in range(2, n + 1):
            fatorial *= i
        return fatorial

numero = int(input("Digite um número: "))
print(f"O fatorial de {numero} é {calcular_fatorial(numero)}")
