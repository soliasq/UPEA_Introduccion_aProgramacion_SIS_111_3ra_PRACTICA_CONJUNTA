import timeit
par=0
impar=0
n=int(input("Ingrese diminsion="))
B=[]
for i in range(n):
    B.append(int(input("ingrese un valor=")))
for i in range(n):
    if B[i]%2==0:
        par = par + B[i]
    else:
        impar = impar + B[i]
# mostrando vector
print(B,"")
#mostrando suma     
print("la suma de v[n pares]=",par)
print("la suma de v[n impares]=",impar)
total_time= timeit.timeit( number=1000)  