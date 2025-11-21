# Funciones

"""
def my_function(input): 
    #donde va el input van los parámetros, se puede dejar en blanco.
    ...
    ...
    return output #input y output son OPCIONALES.

#Este es un docstring de módulo
#Vamos a crear varias funciones


def saludar():
    "Es una función que va a saludar."
    nombre = "Alvin"
    apellido = "Portilo"
    nombre_completo = f"{nombre.title()} {apellido.title()}" #title pone la inicial mayúscula.
    print(f"Hola {nombre_completo}")
"""

"""
def saludar():
    "Es una función que va a saludar."
    nombre = input("Digite el nombre: ")
    apellido = input("Digite el apellido: ")
    nombre_completo = f"{nombre.upper()} {apellido.upper()}"
    print(f"Hola {nombre_completo}")
"""

"""
def saludar_con_parámetro(nombre,apellido):
    "Es una función que va a saludar."
    
    print(f"Hola {nombre.title()} {apellido.title()}")
saludar_con_parámetro("Fer", "calvo")
"""