numero = int(input("Digite um número: "))
vetor = []

for i in range(1, numero + 1):
    vetor.append(i * 2)

print(f"Dobro dos números de 1 até {numero}: {vetor[::]} \n")