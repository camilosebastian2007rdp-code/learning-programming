palabra = input("Palabra secreta: ").lower()

vidas = 6
adivinadas = []

while vidas > 0:

    letra = input("Ingrese una letra: ").lower()

    if letra in palabra:
        adivinadas.append(letra)
    else:
        vidas -= 1

    for caracter in palabra:

        if caracter in adivinadas:
            print(caracter, end=" ")
        else:
            print("_", end=" ")

    print("\nVidas:", vidas)

    gano = True

    for caracter in palabra:
        if caracter not in adivinadas:
            gano = False

    if gano:
        print("Ganaste")
        break

if vidas == 0:
    print("Perdiste")