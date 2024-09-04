
n = -1
x=-1
con=0
aux=0
import timeit
B=[]
C=[]
# Simulación de do...while
while True:
    n = int(input("Introduce un número positivo= "))
    if n> 0:
        break
    print("El número debe ser positivo. Inténtalo de nuevo.")

for i in range(n):
    x = int(input("Introduce valor en= "))
    B.append(x)
print("Vector llenado")
print(B)
#intercambiar posiciones por el segundo y penultimo
aux=B[con+1]
B[con+1]=B[n-2]
B[n-2]=aux
#mostramos vector intercambiaso posiciones
print("Vector final ")
print(B)

total_time= timeit.timeit( number=1000)
print("tiempo en ejecucion",total_time)