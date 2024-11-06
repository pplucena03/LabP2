numero = int(input('Digite um número inteiro: '))

if numero < 0:
    print('Número inválido!')

divisores = 0

for i in range(1, (numero + 1)):
    if numero % i == 0:
        divisores += 1

if divisores == 2:
    print('Número primo')
else:
    print('Número não primo')