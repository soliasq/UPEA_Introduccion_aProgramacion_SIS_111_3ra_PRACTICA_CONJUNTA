n = -1
contar=0
import timeit
B=[]
C=[]
A=[]
# Simulación de do...while
while True:
    n = int(input("Introduce un número positivo: "))
    if n> 0:
        break
    print("El número debe ser positivo. Inténtalo de nuevo.")

print(f"Has ingresado un número positivo: {n}")

for i in range(n):
    x=int(input("Ingrese un valor="))
    A.append(x)
for i in range(n):
    y=int(input("Ingrese un valor="))
    B.append(y)
for i in range(n):
    C.append(A[i]*B[i])
print("Mostrando vector multiplicado")
print(C)
total_time= timeit.timeit( number=1000)
print("tiempo en ejecucion",total_time)