print('Bem-vindo(a) ao interrogatório. Digite "s" para Sim e "n" para Não.')

perguntas = ['Telefonou para vítima? ', 'Esteve no local do crime? ', 'Mora perto da vítima? ', 'Devia para vítima? ', 'Já trabalhou com a vítima? ']

sim = 0

for i in perguntas:
  resposta = input(i)
  if resposta == 's':
    sim += 1

if sim <= 2:
  print('Suspeito')
elif sim == 3 or sim == 4:
  print('Cúmplice')
else:
  print('Assassino')