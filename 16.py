
n = -1
a=-1
b=1
c=0
import timeit
B=[]
# Simulación de do...while
while True:
    n = int(input("Introduce un número positivo= "))
    if n> 0:
        break
    print("El número debe ser positivo. Inténtalo de nuevo.")

for i in range(n):

    c=a+b
    B.append(c)
    a=b
    b=c
print("serie fifo")
print(B)


total_time= timeit.timeit( number=1000)
print("tiempo en ejecucion",total_time)