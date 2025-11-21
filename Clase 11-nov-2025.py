#Este módulo va a contener funciones

#Una función tiene dos tiempos, una definición y una llamada

#Vamos a definir una función
def mi_funcion():
    """Esta función imprime un saludo"""
    print("hola mundo")
    print("amigo usuario")
    print("gracias por usar nuestro sistema!")
    
#Vamos a recibir información desde afuera de la función
def capturar_nombre():
    """Esta función recibe valores por medio de input"""
    nombre_input = input("Escriba su nombre: ")
    apellido_input = input("Escriba su apellido: ")
    nombre_completo = f"{nombre_input.capitalize()} {apellido_input.capitalize()}"
    print(nombre_completo)
    
def capturar_usuario(nombre, edad):
    """Esta función recibe valores por medio de argumentos."""
    nombre_usuario = nombre
    edad_usuario = edad
    texto = f"{nombre_usuario.title()} tiene {edad_usuario} años de edad."
    print(texto)
    
#Llamando la función captura_nombre
capturar_usuario(input("Ingrese su nombre: "), input("Ingrese su edad: "))

#Función que devuelve un valor

def calculo_impuesto(ventas):
    """Esta función captura el valor del impuesto."""
    if ventas < 500:
        tasa_impuesto = 0.1
    else:
        tasa_impuesto = 0.25
    return tasa_impuesto

ventas = 1000
#Aquí vamos a llamar a la función
tasa_calculada = calculo_impuesto(ventas)
monto_impuesto = calculo_impuesto(ventas)*ventas
print(f"""El valor de la venta fue de ${ventas:,.2f},
      la tasa de impuesto es {tasa_calculada:.2f},
      y el monto por tanto es ${monto_impuesto:,.2f}""")