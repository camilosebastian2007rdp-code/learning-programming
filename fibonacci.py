n1 = 0
n2 = 1

contador = 1

while contador <= 20:
    print(n1)
    aux = n1 + n2
    n1 = n2
    n2 = aux
    contador += 1