letra = input("Columna (a-h): ").lower()
fila = int(input("Fila (1-8): "))

columnas = {
    "a":1,"b":2,"c":3,"d":4,
    "e":5,"f":6,"g":7,"h":8
}

columna = columnas[letra]

derecha = 8 - columna
izquierda = columna - 1
arriba = 8 - fila
abajo = fila - 1

print("Derecha:", derecha)
print("Izquierda:", izquierda)
print("Arriba:", arriba)
print("Abajo:", abajo)

print("Diagonal derecha arriba:", min(derecha, arriba))
print("Diagonal izquierda arriba:", min(izquierda, arriba))
print("Diagonal derecha abajo:", min(derecha, abajo))
print("Diagonal izquierda abajo:", min(izquierda, abajo))