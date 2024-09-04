import timeit
par=0
n=int(input("Ingrese diminsion="))
B=[]
for i in range(n):
    B.append(int(input("ingrese un valor=")))
    # mostrando vector
print(B, "")
for i in range(n):
    if B[i]%2==0:
        B[i]=0
        print("B[",i,"]=",B[i])
print(B)
total_time= timeit.timeit( number=1000)
print("tiempo en ejecucion",total_time)