def polaridade_do_numero(numero):
    if numero > 0:
        print('P')
    elif numero <= 0:
        print('N')

  
num = int(input("Digite um número: "))
polaridade_do_numero(num)