turno = input('Em que turno você estuda? Digite "M" para Matutino, "V" para Vespertino e "N" para Noturno: ').lower()

if turno == 'm':
  print('Bom dia!')
elif turno == 'v':
  print('Boa tarde!')
elif turno == 'n':
  print('Boa noite!')
else: 
  print("Dígito inválido.")