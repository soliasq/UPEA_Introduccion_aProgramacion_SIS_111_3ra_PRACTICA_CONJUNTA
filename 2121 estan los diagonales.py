
f = -1
import timeit
impar=1
M=[]

# Simulación de do...while
while True:
    f = int(input("Introduce número filas= "))
    c = int(input("Introduce número columnas= "))
    if f> 0:
        break
    print("El número debe ser positivo. Inténtalo de nuevo.")
#B = [0][0] * n*m
for i in range(f):
    Fila=[]
    for j in range(c):
        if i>=j:
            Fila.append(1)
        else:
            Fila.append(0)

    M.append(Fila)


print("la matriz es=")
#print(M,end="")
for filass in M:
    print( filass)

total_time= timeit.timeit( number=1000)
print("tiempo en ejecucion",total_time)

# Dimensiones de la matriz
n = 3  # Puedes cambiar el tamaño de la matriz aquí

# Inicializar la matriz con ceros
matriz = [[0] * n for _ in range(n)]

# Llenar la matriz diagonal inferior
for i in range(n):
    for j in range(i + 1):
        matriz[i][j] = int(input(f"Ingrese el valor para la posición [{i}][{j}]: "))

# Mostrar la matriz
print("La matriz diagonal inferior es:")
for fila in matriz:
    print(fila)
# Dimensiones de la matriz
n = 4  # Tamaño de la matriz

# Inicializar la matriz con ceros
matriz = [[0] * n for _ in range(n)]

# Llenar la parte triangular inferior (sin incluir la diagonal principal)
for i in range(n):
    for j in range(i):
        matriz[i][j] = i + j  # Puede cambiarse la lógica según se necesite

# Mostrar la matriz
print("La matriz triangular inferior (sin incluir la diagonal principal) es:")
for fila in matriz:
    print(fila)

    # Dimensiones de la matriz
    n = 4  # Tamaño de la matriz

    # Inicializar la matriz con ceros
    matriz = [[0] * n for _ in range(n)]

    # Llenar la parte triangular inferior (sin incluir la diagonal principal)
    for i in range(n):
        for j in range(i):
            matriz[i][j] = i + j  # Puede cambiarse la lógica según se necesite

    # Mostrar la matriz en orden inverso (de abajo hacia arriba)
    print("La matriz triangular inferior (sin incluir la diagonal principal) en orden inverso es:")
    for i in range(n - 1, -1, -1):
        for j in range(n):
            print(matriz[i][j], end=' ')
        print()

# Dimensiones de la matriz
n = 4  # Tamaño de la matriz

# Inicializar la matriz con ceros
matriz = [[0] * n for _ in range(n)]

# Llenar la parte triangular superior (sin incluir la diagonal principal)
for i in range(n):
    for j in range(i + 1, n):
        matriz[i][j] = i + j  # Puede cambiarse la lógica según se necesite

# Mostrar la matriz
print("La matriz triangular superior (sin incluir la diagonal principal) es:")
for fila in matriz:
    print(fila)
