soma_notas = 0

for i in range(1,4):
    nota = float(input(f'Digite a {i}º nota: '))
    soma_notas += nota

media = round((soma_notas / 3), 1)

print(f'Média = {media}')

if media >= 7:
  print('Aprovado')
elif media < 7 and media >= 4:
  print('Reposição')
else:
  print('Reprovado') 