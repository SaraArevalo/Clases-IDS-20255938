#Ejercicio 1

"""N = int(input())
if N >= 0:
    print ("Positivo")
else:
    print ("Negativo")"""
    
#Ejercicio 2
"""
S = int(input())
if S%2 == 0:
    S_par = S + 2
else:
    S_par = S + 1
if S%2 == 0:
    S_impar = S-1
else:
    S_impar = S-2 
print(S_par, S_impar)
"""

#Ejercicio 3
"""
N = int(input())
listaN = []
for i in range(N):
    listaN.append(int(input()))
n_7 = listaN.count(7)
n_5 = listaN.count(5)
print(n_7, n_5)
"""

#Ejercicio 4
"""
N = int(input())
A, B, C = map(int, input().split())
for i in range(N):
    combo = input().strip()
    daño = 0
    for ataque in combo:
        if ataque == 'A':
            daño = daño + A
        elif ataque == 'B':
            daño = daño + B
        elif ataque == 'C':
            daño = daño + C
    print (daño)
"""

#Ejercicio 4
"""
N = int(input())
listaN = []
for i in range(N):
    listaN.append(input())
for nombre in listaN:
    if len(nombre) <= 6:
        print("No vale la pena")
    elif len(nombre) >= 8:
        print("Si aguanto otro desarrollo de personaje")
    elif len(nombre) > 6 and len(nombre) < 8:
        print("Dios no creo aguantar esta vez")
"""

#Ejercicio 5
"""
x, y = map(int,input().split())
if x > y:
    print(x)
else:
    print(y)
"""

#Ejercicio 6
"""
A = int(input())
edades = []
for i in range(A):
    edades.append(int(input()))
    personas = 0
for edad in edades:
    if edad >= 15:
        personas = personas + 1
    else:
        personas = personas + 0
print(personas)
"""

#Ejercicio 7
"""
entrada = input("conectado o desconectado").lower
if entrada == "conectado":
    print("Ola Ivan")
else:
    print("Ol..")
"""

#Ejercicio 8

N = int(input())
for i in range(N):
    P = int(input())
    if P >= 3:
        print("Ok")
    else:
        print("No")
