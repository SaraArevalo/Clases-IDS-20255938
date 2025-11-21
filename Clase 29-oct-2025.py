#Voy a iniciar mi variable en true
"""
ejecución = True
while ejecución:
    opción = input("Estamos ejecutando el menú? Y/N: ")
    if opción.lower() == "n":
        ejecución = False 
    elif opción.lower() == "y":
        ejecución = True #esto no afecta, más bien es redundante. Sin embargo, sí necesita especificar la opción "yes".
        print("Ok, continuemos.")
    else:
        print("La opción elegida no es válida.")
print("Gracias por utilizar nuestro sistema!!")
"""

#Un pequeño sistema de registro de alumnos

#Configuración inicial
alumnos = 0
lista_alumnos = []
"""
cantidad = int(input("Cuántos alumnos vamos a ingresar? "))

for i in range(cantidad):
    alumno = input("Digite el nombre del pajarito: ")
    lista_alumnos.append(alumno)
print(lista_alumnos)
"""

print("Bienvenido a nuestro sistema de control de Alumnos.")
"""
opción = input("Elija la opción (1: Ingresar alumnos): ")
if opción == "1":
    print("Vamos a ingresar alumnos: ")
"""
menú_activo = True
while menú_activo:
    opción = input("Elija la opción (1: Ingresar alumno, 5: Salir):")
    if opción == "5":
        menú_activo = False
    elif opción == "1":
        alumno = input("Nombre de alumno a agregar: ")
        lista_alumnos.append(alumno)
    elif opción == "2":
        i = int(input("Ingrese la posición del alumno a modificar: "))
        n = input("Ingrese el nuevo nombre del alumno: ")
        lista_alumnos[i-1] = n 
    elif opción == "4":
        borrado = lista_alumnos.pop(int(input("Ingrese el número del alumno a popear(1-4): ")))
        print(f"Usted ha popeado a {borrado}.")
print("Gracias por utilizar nuestro Sistema.")