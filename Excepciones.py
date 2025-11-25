"""def calcular_impuesto():
    pass"""

while True: # Se va a ejecutar hasta que se calcule bien.
    try:
        monto = int(input("Monto a calcular: ")) # el error(excepción) se genera aquí.
    except:
        print("Ese tipo de valores no es válido.")
    else:
        impuesto = monto + 25
        print(f"El valor del impuesto es de ${impuesto:,.2f}")
        break #Esto es para que el while se deje de ejecutar una vez haga lo que necesitamos.
    finally:
        print("Hemos terminado la ejecución de esta pregunta.")
        # El break no se pone en el finally porque este se ejecuta sin importar si da error o no.
        # Por lo que no tiene sentido que el bucle termine ahí.