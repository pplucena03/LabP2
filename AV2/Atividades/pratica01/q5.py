#questão após a de autenticação

import re

def numero_de_vogais(string):
    total = re.findall('[aeiou]', string)
    return len(total)

string = input("Digite alguma coisa: ")
print(f"Vogais: {numero_de_vogais(string)}")