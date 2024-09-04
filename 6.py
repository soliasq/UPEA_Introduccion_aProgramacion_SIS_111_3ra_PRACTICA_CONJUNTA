


import timeit
nomul=0
contar=0
n=int(input("Ingrese diminsion="))
B=[]
for i in range(n):
    B.append(int(input("ingrese un valor=")))
    # mostrando vector
print(B, "")
for i in range(n):
    if B[i]%5==0:
        contar=contar+1
    else:
        nomul=nomul+1
print(B)
print("total mutiplos de 5=",contar)
print("total no multiplos=",nomul)
total_time= timeit.timeit( number=1000)
print("tiempo en ejecucion",total_time)