# Diccionarios

#Vamos a crear un diccionario
"""
mi_gato = {"nombre": "pelusa", 
           "edad": 3, 
           "personalidad": "tonto"}
abys_cat = {
    "personalidad": "simpático",
    "nombre": "peluza",
    "edad": 3
}
copia = mi_gato == abys_cat
print(copia)
"""

"""
birthdays = {
    "Alice": "Apr 1",
    "Bob": "Dec 12",
    "Carol": "Mar 4"
}

birthdays["Carol"] = "Abr 21"
print(birthdays["Carol"])
birthdays["Fer"] = "Mar 3"

for persona, fecha in birthdays.items():
    print(f"El cumpleaños de {persona} es en {fecha}")

print(birthdays)
del birthdays["Bob"]
print(birthdays)
"""

semana = {}
semana["uno"] = "lunes"
semana["dos"] = "martes"
semana["tres"] = "miércoles"
semana["cuatro"] = "jueves"
semana["cinco"] = "viernes"
print(semana)

for k, v in semana.items():
    print(v)