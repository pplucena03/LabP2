from random import randint

def media(lista):
    total = 0

    for i in lista:
        total += i

    total /= 3
    
    print(lista)
    print(f"A media dos numeros é: {total:.1f}")

lista = []

#gera uma lista aleatoria
for i in range(0, 3):
    num = randint(1, 11)
    lista.append(num)

media(lista)