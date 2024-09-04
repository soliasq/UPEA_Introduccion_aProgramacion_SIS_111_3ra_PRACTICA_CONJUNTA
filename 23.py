n= -1
import timeit
sdp=0
sds=0
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
    for j in range(n):
        print(i,j)
        if i==j:
                sdp = sdp + M[i][j]
for i in range(n):
    for j in range(n):
       if(i + j) == (n - 1):
            sds = sds + M[i][j]
            print(sdp)
for filass in M:
    print( filass)

# para mostrar matriz
print("la matriz es=")
#print(M,end="")
for filass in M:
    print( filass)
print("Suma Diagonal principal=",sdp)
print("Suma Diagonal secundario=",sds)
total_time= timeit.timeit( number=1000)
print("tiempo en ejecucion",total_time)