f = -1
import timeit
impar=1
#M=[]
cc=1
j=0
# Simulación de do...while
while True:
    f = int(input("Introduce número filas= "))
    M = [[0] * f for _ in range(f)]
    c = int(input("Introduce número columnas= "))
    if f> 0:
        break
    print("El número debe ser positivo. Inténtalo de nuevo.")
#B = [0][0] * n*m
print(M)
for i in range(f):

    if(i%2==0):
        for j in range(f):
            M[i][j]=cc
            cc=cc+1
    else:
        for j in range(c-1,-1,-1):
            print (j,"=",i)
            M[i][j]=cc
            cc = cc + 1



print("la matriz es=")
#print(M,end="")
for filass in M:
    print( filass)

total_time= timeit.timeit( number=1000)
print("tiempo en ejecucion",total_time)