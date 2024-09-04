
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
    for i in range(c):
        x= int(input("Introduce un valor= "))
        Fila.append(x)
    M.append(Fila)


print("la matriz es=")
print(M)
total_time= timeit.timeit( number=1000)
print("tiempo en ejecucion",total_time)