nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = round(((nota1 + nota2) / 2), 1)

print(f'Média = {media}')

if media == 10:
  print('Aprovado com distinção')
elif media >= 7:
  print('Aprovado')
else:
  print('Reprovado')