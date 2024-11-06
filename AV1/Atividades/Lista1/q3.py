letra = input('Digite uma letra: ').lower()
vogais = ['a', 'e', 'i', 'o', 'u']

if letra in vogais:
  print('Essa letra é uma vogal')
else:
  print('Essa letra é consoante')