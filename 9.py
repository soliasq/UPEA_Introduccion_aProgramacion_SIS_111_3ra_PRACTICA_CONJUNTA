

n = -1
dim=0
import timeit
B=[]
A=[]
# Simulación de do...while
while True:
    n = int(input("Introduce un número positivo: "))
    if n> 0:
        break
    print("El número debe ser positivo. Inténtalo de nuevo.")

print(f"Has ingresado un número positivo: {n}")
#llenado de vector de dimension n
for i in range(n):
    x=int(input("Ingrese un valor="))
    A.append(x)
#invertit vector A[] en B[]
for i in range(n-1,-1,-1):
    B.append(A[i])
    dim=dim+1


print("Mostrando vector A")
print(A)
print("Mostrando vector B invertido")
print(B)
print("Mostrando dimincion de vector=",dim)

total_time= timeit.timeit( number=1000)
print("tiempo en ejecucion",total_time)