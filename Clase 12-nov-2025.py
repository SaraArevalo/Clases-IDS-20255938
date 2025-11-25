# Vamos a crear una función utilzando kwargs
# Args es para crear listas y kwargs para diccionarios.
# args es con un * y kwargs es con dos.

def registro_profesores(nombre, apellido, **materias):
    """Crear un registro de profesor, utilizando kwargs."""
    print(f"El profesor {nombre} {apellido}, imparte las materias:")
# Para recorrer un diccionario con for se debe descomponer
# sus partes en clave - valor y se recorre con .items
    for ciclo, materias in materias.items:
        print(f"\t - {ciclo}: \t {materias}")
registro_profesores(
    "Alvin", 
    "Portillo",
    Ciclo1 = ["BD1", "IIJ", "A&GD"],
    Ciclo2 = ["DAI", "BD2", "SINE"],
    Ciclo3 = ["IDS", "FPEN", "PAD"]
)
