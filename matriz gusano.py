def generar_matriz_gusanito(n, m):
    matriz = [[0] * m for _ in range(n)]
    valor = 1
    for i in range(n):
        if i % 2 == 0:
            # Llenar de izquierda a derecha
            for j in range(m):
                matriz[i][j] = valor
                valor += 1
        else:
            # Llenar de derecha a izquierda
            for j in range(m - 1, -1, -1):
                matriz[i][j] = valor
                valor += 1
    return matriz

def mostrar_matriz(matriz):
    for fila in matriz:
        print(' '.join(map(str, fila)))

# Tamaño de la matriz
n = 4
m = 5

matriz_gusanito = generar_matriz_gusanito(n, m)
print("La matriz gusanito es:")
mostrar_matriz(matriz_gusanito)