numero = int(input("Digite um número: "))
vetor = []

for i in range(1, numero + 1):
    vetor.append(i)

print(f"Números pares até {numero}: {vetor[1::2]} \n")
print(f"Números ímpares até {numero}: {vetor[::2]} \n")