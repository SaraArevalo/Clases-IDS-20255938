datos = [1,2,"tres", ["lunes", "martes", "miércoles"]]
print(datos[1])
print(datos[2])
print(datos[2][1]) #para extraer la letra r de la palabra tres
print(datos[3][2][3]) #para extraer la letra r de miércoles o print(datos[-1][-1][3])

numeros = ["uno", "dos", "tres"]
print (numeros)
numeros = numeros + ["cuatro", "cinco", "seis"]
print (numeros)
print (len(numeros))
numeros[2] = "trois"
print (numeros) #las listas son objetos, los cuales tienen propiedades y métodos.
numeros.append(input("Escriba el siguiente número: "))
print(numeros)
numeros.insert(2, input("Einender nummer: "))
print(numeros)