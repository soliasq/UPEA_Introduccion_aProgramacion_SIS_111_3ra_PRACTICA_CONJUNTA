c= -1
import timeit
suma=0
M=[]
# Simulación de do...while
while True:
    c= int(input("Introduce filas= "))
    f = int(input("Introduce columnas= "))

    if c> 0:
        break
    print("El número debe ser positivo. Inténtalo de nuevo.")
#B = [0][0] * n*m

for i in range(c):
    Fila=[]
    for j in range(f):
        x = int(input("Introduce filas="))
        Fila.append(x)
    M.append(Fila)

for i in range(f):
    for j in range(c):
        suma = suma+ M[i][j]


# para mostrar matriz
print("la matriz es=")
#print(M,end="")
for filass in M:
    print( filass)
print("suma fila es=",suma)
total_time= timeit.timeit( number=1000)
print("tiempo en ejecucion",total_time)