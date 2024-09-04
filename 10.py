n = -1
dim=0
import timeit
A=[]
# Simulación de do...while
while True:
    n = int(input("Introduce un número positivo: "))
    if n> 0:
        break
    print("El número debe ser positivo. Inténtalo de nuevo.")

print(f"Has ingresado un número positivo: {n}")
#llenado de vector de dimension n
for i in range(1,n):
    A.append(i*i)
print("Mostrando vector A")
print(A)
total_time= timeit.timeit( number=1000)
print("tiempo en ejecucion",total_time)