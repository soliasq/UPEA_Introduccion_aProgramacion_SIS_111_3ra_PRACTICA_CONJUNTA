
n = -1
con=0
base=1
import timeit
B=[]
# Simulación de do...while
while True:
    n = int(input("Introduce un número positivo= "))
    x = int(input("Ingrese base de potencia= "))
    if n> 0:
        break
    print("El número debe ser positivo. Inténtalo de nuevo.")

for i in range(1,n+1):
    #print("vale i",i)
    for j in range(i):
        base=base*x
    B.append(base)
    base=1
print("Vector llenado")
print(B)
