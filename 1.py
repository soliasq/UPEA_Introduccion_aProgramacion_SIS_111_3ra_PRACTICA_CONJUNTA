import timeit
s=0
n=int(input("Ingrese diminsion="))
B=[]
for i  in range(n):
    B.append(int(input("ingrese un valor")))
for i  in range(n):
    s=s+B[i]
# mostrando vector
print(B,"")
#mostrando suma     
print("la suma de v[nelementos]=",s) 
total_time= timeit.timeit( number=1000)  