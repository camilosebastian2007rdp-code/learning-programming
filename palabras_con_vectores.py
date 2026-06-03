vector = []

opcion = 0

while opcion != 4:

    print("\n1. Guardar palabra")
    print("2. Mostrar palabra")
    print("3. Mostrar invertida")
    print("4. Salir")

    opcion = int(input("Opción: "))

    if opcion == 1:

        cantidad = int(input("Cantidad de letras: "))
        vector.clear()

        for i in range(cantidad):
            vector.append(input("Letra: "))

    elif opcion == 2:

        for letra in vector:
            print(letra, end="")
        print()

    elif opcion == 3:

        for i in range(len(vector)-1, -1, -1):
            print(vector[i], end="")
        print()