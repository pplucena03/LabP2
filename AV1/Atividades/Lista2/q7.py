nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
salario = int(input('Digite seu salário: '))
sexo = input('Digite seu sexo [M ou F]: ').lower()
estado_civil = input('Digite seu estado civil [S, C ,V ou D]: ').lower()

if len(nome) < 3:
    print('O nome deve conter mais de 3 caracteres!')

if idade < 0 or idade > 150:
    print('Idade inválida')

if salario <= 0:
    print('Salário inválido')

if sexo != 'm' and sexo != 'f':
    print('Caracter de sexo inválido')

if estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd':
    print('Caracter de estado civil inválido')