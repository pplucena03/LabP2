print('Bem-vindo ao somador!')

continuar = 's'

while continuar == 's':
    numero1 = int(input('Digite um número: '))
    numero2 = int(input('Digite outro número: '))

    print(f'{numero1} + {numero2} = {numero1 + numero2}')

    continuar = input('Deseja fazer outra soma? [S ou N] \n Resposta: ').lower()