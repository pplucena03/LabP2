import random

N = []

for i in range(10):
    i = random.randint(0, 1000)
    N.append(i)

maior_valor = max(N)
menor_valor = min(N)
soma = maior_valor + menor_valor

print(f'O maior valor é: {maior_valor} \nO menor valor é: {menor_valor} \nA soma deles é: {soma}')