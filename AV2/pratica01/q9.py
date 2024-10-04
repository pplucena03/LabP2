import re

def numero_de_palavras(string):
    
    total = re.findall('[ ]', string)

    print(f"Total de palavras: {len(total) + 1}")

string = 'essa é uma frase de teste que contém 10 palavras'
numero_de_palavras(string)