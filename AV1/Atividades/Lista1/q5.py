numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))

if numero1 > numero2 and numero1 > numero3:
  print(f'O número {numero1} é maior que {numero2} e {numero3}')
elif numero2 > numero1 and numero2 > numero3:
  print(f'O número {numero2} é maior que {numero1} e {numero3}')
elif numero3 > numero1 and numero3 > numero2:
  print(f'O número {numero3} é maior que {numero1} e {numero2}')
else:
  print('Os números são iguais')