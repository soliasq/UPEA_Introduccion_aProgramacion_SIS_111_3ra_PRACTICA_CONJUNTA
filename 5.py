mport timeit
par=0
impar=0
n=int(input("Ingrese diminsion="))
B=[]
for i in range(n):
    B.append(int(input("ingrese un valor=")))
    # mostrando vector
print(B, "")
for i in range(n):
    if B[i]%2==0:
        par=par+1
    else:
        impar=impar+1
print(B)
print("totalpares=",par)
print("total Impares=",impar)
total_time= timeit.timeit( number=1000)
print("tiempo en ejecucion",total_time)