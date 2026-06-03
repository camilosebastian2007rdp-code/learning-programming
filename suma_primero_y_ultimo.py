vector = []

cantidad = int(input("Cantidad de números: "))

for i in range(cantidad):

    numero = int(input("Número: "))

    while len(vector) > 0 and numero == vector[0] + vector[-1]:

        print("No permitido")
        numero = int(input("Digite otro número: "))

    vector.append(numero)

print("Vector final:")
print(vector)