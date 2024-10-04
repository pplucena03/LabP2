tentativas = 0

while True:
    login_usuario = input('Digite o login: ')
    senha_usuario = input('Digite a senha: ')

    if senha_usuario == 'admin' and login_usuario == 'admin':
        print('Logado com sucesso!')
        break
    
    if login_usuario != 'admin':
        print('Usuário incorreto! Tente novamente \n')
        tentativas += 1

    elif senha_usuario != 'admin':
        print('Senha incorreta! Tente novamente \n')
        tentativas += 1

    if tentativas == 3:
        print('1 tentativa restante\n')

    if tentativas == 4:
        print('Usuário bloqueado!')
        break