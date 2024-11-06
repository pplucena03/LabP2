i = 0
nota = 0
total = 0

while i < 3:
  nota = int(input('Digite o valor da nota: '))
  total += nota
  i += 1

media = total / 3
print(f'A média é: {media}')