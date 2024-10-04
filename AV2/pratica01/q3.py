num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))
operacao = input("Digite '+' para somar, '-' para subtrair, '*' para multiplicar ou '/' para dividir: ")

if operacao == '+':
    total = num1 + num2
    print(f"{num1} + {num2} = {total}")

elif operacao == '-':
    total = num1 - num2
    print(f"{num1} - {num2} = {total}")

elif operacao == '*':
    total = num1 * num2
    print(f"{num1} * {num2} = {total}")

elif operacao == '/':
    total = num1 / num2
    print(f"{num1} / {num2} = {total}")

else:
    print("Operação inválida")