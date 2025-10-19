#ejercicios sobre tuplas

tupla1 = (1,12,255,1289,60,000) #inmutable
lista1 = [1,12,255,1289,60,000] #mutable
lista1[-1] = 3
print (lista1)

print(len(tupla1))
print(tupla1[4]) #recuperar el elemento 5 (Indice 4) empezando de 0
print(tupla1[3:])

print(tupla1[-1])  #el -1 hace referencia al ultimo elemento
tupla1[-1] = 3
print(tupla1)

