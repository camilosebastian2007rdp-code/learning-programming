numero = int(input("Digite un número: "))

resultado = 1
contador = numero

while contador > 0:
    resultado *= contador
    contador -= 1

print("Factorial:", resultado)