# Este módulo contendrá las funciones.

# Definiendo la función.

def ordenar_pizza(size, masa, *ingredientes): 
    """Vamos a imprimir su orden"""
    print(f"Usted a ordenado una pizza {size} de masa {masa} de:")
    for i in ingredientes:
        print(f"\t- {i}") 
        
def registro_profesores(nombre, apellido, **materias):
    """Crear un registro de profesor, utilizando kwargs."""
    print(f"El profesor {nombre} {apellido}, imparte las materias:")
# Para recorrer un diccionario con for se debe descomponer
# sus partes en clave - valor y se recorre con .items
    for ciclo, materias in materias.items:
        print(f"\t - {ciclo}: \t {materias}")
        
def saludar_usuarios(nombres):
    """Saludará usuario"""
    for nombre in nombres:
        print(f"Hola, {nombre.capitalize()}")

