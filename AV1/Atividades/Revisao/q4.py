def converter_para_fahrenheit(temp):
  resultado = (temp * 9/5) + 32

  return resultado

def converter_para_celsius(temp):
  resultado = (temp - 32) * 5/9

  return resultado

selecionar_escala = int(input("Digite '1' para converter de C° para F° ou '2' para o contrário: "))

if selecionar_escala != 1 and selecionar_escala != 2:
  print("Valor inserido inválido!")
  exit()

resultado = 0
  
if selecionar_escala == 1:
  temperatura = float(input("Digite a temperatura em Celsius: "))
  resultado = converter_para_fahrenheit(temperatura)
  print(f"A temperatura em Fahrenheit é: {resultado}")
  
else:
  temperatura = float(input("Digite a temperatura em Fahrenheit: "))
  resultado = converter_para_celsius(temperatura)
  print(f"A temperatura em Celsius é: {resultado}")