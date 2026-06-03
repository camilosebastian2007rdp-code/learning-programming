acumulado = 0

while acumulado <= 100:

    valor = int(input("Ingrese número: "))
    acumulado += valor

    print("Suma actual:", acumulado)

print("La suma superó 100")