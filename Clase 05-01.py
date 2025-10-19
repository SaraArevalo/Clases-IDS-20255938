nombre = "Alvin" #5caracteres
palabra = "RECONOCER" #contiene el 0; es decir, R(0) E(1) y así sucesivamente. Si llega hasta el 8 es porque tiene 9 caracteres
otra_palabra = "palabra"

"""print(len(nombre))

print(nombre[2])
print(nombre[2:])""" #presentar hasta el último caracter, omitir el final


print(len(palabra))
print(palabra[4:8])
print(palabra[4:])
print(palabra[1::2])
print(palabra[0::2])
print(palabra[::3]) #para omitir desde el principio
print(palabra[::])
print(palabra[::-1])
print(otra_palabra[::-1])

#########

"""palabra = "sorbete"

print(palabra==palabra[::-1]) #comparar ==, comparar si la palabra es palíndromo

palabra = "oro"
print(palabra==palabra[::-1])"""

#######

mi_palabra = "jocote"
print(mi_palabra)
mi_palabra_mayuscula = mi_palabra.upper()
print(mi_palabra_mayuscula)
#el punto es una union de dependencia 

mi_palabra_cap = mi_palabra.capitalize()
print(mi_palabra_cap)
