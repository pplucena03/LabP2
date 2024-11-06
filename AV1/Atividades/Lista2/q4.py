#O nome do arquivo está como questão 4 mas essa é a questão 1 dos desafios. Os próximos seguem na ordem :)

num_anterior = 0
num_atual = 1
proximo_num = 0

while num_atual < 500:
    print(f'{num_atual}')
    
    proximo_num = num_anterior + num_atual

    num_anterior = num_atual
    
    num_atual = proximo_num