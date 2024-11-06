from lista import usuarios

def validar_user(login, senha):
    tamanho_lista = len(usuarios)

    for i in range(0, tamanho_lista):
        if usuarios[i]['username'] == login and usuarios[i]['senha'] == senha:
            return True
        
login = input("Digite o username: ")
senha = input("Digite a senha: ")

if validar_user(login, senha):
    print("Acesso permitido")
else:
    print("Acesso negado")