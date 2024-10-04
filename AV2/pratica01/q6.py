def fatorial(num):
    total = 1

    for i in range(1, num + 1):       
        total *= i

    print(f"O fatorial de {num} é {total}")

num = int(input("Digite um número: "))
fatorial(num)