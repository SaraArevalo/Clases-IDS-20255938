#listas 2

"""nombre = "Antonio"
repetidos = nombre.lower().count("a")
print (repetidos)"""

"""nombres = ["Ana", "Antonio", "Ana","José"]

r_a = 0
print(nombres.count("José"))
r_a = r_a + nombres[0].lower().count("a")
r_a = r_a + nombres[1].lower().count("a")
r_a = r_a + nombres[2].lower().count("a")
r_a = r_a + nombres[3].lower().count("a")
print(r_a)

print(nombres.index("Ana",1)) o int(nombres.index("Ana",nombres.index("Ana")+1))"""

#listas 3

"""nombres = ["Ana", "Antonio", "Ana", "Jose", "Carlos"]
print(nombres.append("Aby"))
nombres.insert(2, "Jorge")
print(nombres)
nombres.insert(int(input("Posición: ")),input("Nombre nuevo: "))
print(nombres)
posición = int(input("Posición sustituir: "))
nombres[posición] = input("Nombre nuevo sustituir: ") #para sustituir nombres en la lista
print(nombres)
nombres.remove("Carlos") #para remover nombres en la lista
print(nombres)
nombre_borrado = nombres.pop(3)
print(f"Nombre borrado: {nombre_borrado}")
print(nombres)
nombres.reverse()
print(nombres)"""

#if

"""número = 6
captura = int(input("Adivina el número (un intento): "))
if captura == número:
    print("Le acertaste!")
else:
    print("Ese número no era.")
    print("Puedes seguir jugando.")"""
    
#if2

nota = int(input("Digite la nota: "))
if nota > 8:
    print ("Excelente")
elif nota > 6:
    print ("Bueno")
elif nota > 4:
    print ("Regular")
else: 
    print("Malo")

