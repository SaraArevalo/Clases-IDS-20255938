# Vamos a proceder a atender pedidos.

def ordenar_pizza(size, masa, *ingredientes): #ahora con args, estos parámetros VAN SIEMPRE AL FINAL
    """Vamos a imprimir su orden"""
    print(f"Usted a ordenado una pizza {size} de masa {masa} de:")
    for i in ingredientes:
        print(f"\t- {i}") #\t es para que al momento de imprimirlo, lo reconozca como una tabulación.
        
# Llamando la función

ordenar_pizza("grande","delgada", "queso", "tocino", "jamón", "carne")