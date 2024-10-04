def numero_primo(num):
    contador = 0

    for i in range(1, num + 1):
        if num % i == 0:
             contador += 1

    if contador == 2:
        return True
   
    else:
        return False 
    
num = int(input("Digite um numero: "))

if numero_primo(num):
    print("Número primo!")
else:
    print("Número não primo.")