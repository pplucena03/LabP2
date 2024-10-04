import re

def validar_email(email):
    if re.search('[@]', email):
        return True

    else:
        return False


#email = input("Digite um email: ")
email = "teste@email.com"

if validar_email(email):
    print("O email possui @")
else:
    print("O email não possui @")
