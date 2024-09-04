n= -1
import timeit
suma=0
M=[]
# Simulación de do...while
while True:
    n= int(input("Introduce matriz cuadrada= "))

    if n> 0:
        break
    print("El número debe ser positivo. Inténtalo de nuevo.")
#B = [0][0] * n*m

for i in range(n):
    Fila=[]
    for j in range(n):
        x = int(input("Introduce filas="))
        Fila.append(x)
    M.append(Fila)

for i in range(n):
    suma=0
    for j in range(n):
        suma = suma+ M[i][j]
    print("suma fila es=",suma)

for filass in M:
    print( filass)

# para mostrar matriz
print("la matriz es=")
#print(M,end="")
for filass in M:
    print( filass)

total_time= timeit.timeit( number=1000)
print("tiempo en ejecucion",total_time)