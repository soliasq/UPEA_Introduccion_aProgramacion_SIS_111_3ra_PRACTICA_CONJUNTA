
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
        if i==j:
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