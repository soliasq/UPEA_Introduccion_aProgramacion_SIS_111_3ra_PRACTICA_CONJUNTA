n = -1
impar=0
par=0
import timeit
A=[]
# Simulación de do...while
while True:
    n = int(input("Introduce un número positivo: "))
    if n> 0:
        break
    print("El número debe ser positivo. Inténtalo de nuevo.")

print(f"Has ingresado un número positivo: {n}")

for fila in range (n):
    m=int(input(F"ingrse un valor {fila}= "))
    A.append(m)
#llenado de vector de dimension n
for i in range(n):
    if A[i]% 2==0:
        par=par+A[i]
    else:
        impar = impar + A[i]
print("Mostrando vector A=")
print(A)
print("Total pares=",par)
print("Total impares=",impar)

total_time= timeit.timeit( number=1000)
print("tiempo en ejecucion",total_time)