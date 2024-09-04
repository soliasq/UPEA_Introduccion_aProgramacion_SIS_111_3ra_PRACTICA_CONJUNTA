
n = -1
x=-1
contar=0
nnumero=0
import timeit
B=[]
C=[]
# Simulación de do...while
while True:
    n = int(input("Introduce un número positivo: "))
    if n> 0:
        break
    print("El número debe ser positivo. Inténtalo de nuevo.")

print(f"Has ingresado un número positivo: {n}")
while True:
    while n>contar:
        x=int(input("Introduce un digito: "))
        if x>=0 and x>=10:
            B.append(x)
            contar = contar + 1
        else:
            print("ingrese numeros mayores a 2 digitos")
            break
            print("El número debe ser mayor igual de 10. Inténtalo de nuevo.")
    print(f"Has ingresado un número correcto: {x}")
    if contar== n:
        break
contar=0
while contar<=n-1:

    numero=B[contar]
    print (contar,"=",B[contar])

    guardar=numero
    while numero>0:
        nn= numero %10
        numero= numero//10
        nnumero= (nnumero*10)+ nn

    if nnumero==guardar:
        capi=B[contar]
        C.append(capi)
    contar = contar + 1
    nnumero=0
print("nuevo vector",C)
total_time= timeit.timeit( number=1000)
print("tiempo en ejecucion",total_time)