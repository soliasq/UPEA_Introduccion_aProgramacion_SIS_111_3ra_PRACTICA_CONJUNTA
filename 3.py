import timeit
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
       print("B[",i,"]=",B[i])
total_time= timeit.timeit( number=1000)