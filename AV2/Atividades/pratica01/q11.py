def converter_temperaturas(temp, escala):
  if escala == 1:
    resultado = (temp * 9/5) + 32
    return resultado
  
  else:
    resultado = (temp - 32) * 5/9
    return resultado
 
escala = int(input("Digite '1' para converter de C° para F° ou '2' para o contrário: "))

if escala != 1 and escala != 2:
  print("Valor inserido inválido!")
  exit()

if escala == 1:
    temp = float(input("Digite a temperatura em Celsius: "))
    resultado = converter_temperaturas(temp, escala)
    print(f"A temperatura é: {resultado:.2f} F°")

else:
    temp = float(input("Digite a temperatura em Fahrenheit: "))
    resultado = converter_temperaturas(temp, escala)
    print(f"A temperatura é: {resultado:.2f} C°")