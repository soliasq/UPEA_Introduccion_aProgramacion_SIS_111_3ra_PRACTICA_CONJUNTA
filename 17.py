
n = -1
import timeit
impar=1
B=[]

# Simulación de do...while
while True:
    n = int(input("Introduce un número positivo= "))
    if n> 0:
        break
    print("El número debe ser positivo. Inténtalo de nuevo.")
B = [0] * n
for i in range(n-1,-1,-1):
    B[i]=impar
    impar=impar+2

print("serie  de impares desc")
print(B)
total_time= timeit.timeit( number=1000)
print("tiempo en ejecucion",total_time)