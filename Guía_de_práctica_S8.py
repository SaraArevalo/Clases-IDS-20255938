clientes = {}
productos = {}
pedidos = {}
opción = int(input("Seleccione una opción: 1. Mostrar productos 2. Agregar producto 3. Registrar nuevo cliente 4. Mostrar clientes 5. Registrar pedido 6. Mostrar pedido del día 7. Mostrar categorías disponibles 8. Salir"))
if opción == 1:
    if len(productos) == 0:
        print("No hay productos registrados.")
    else:
        for i in range(len(productos)):
            print(productos)
if opción == 2:
    código_producto = input("Ingrese código del producto: ").lower()
    nombre_producto = input("Ingrese nombre del producto: ").lower()
    categoría_producto = input("Ingrese categoría del producto: ").lower()
    precio_producto = float(input("Ingrese precio del producto: "))
    productos[código_producto] = {
        "Nombre": nombre_producto
        "Categoría": categoría_producto
        "Precio": precio_producto
    }
for productos in productos.items():
    print(f"Agregado producto: {nombre_producto}, con código: {código_producto}")
    
código_cliente = input("Código de cliente ")
nombre_cliente = input("Ingrese su nombre: ")
correo_cliente = input("Ingrese un correo: ")
número_cliente = input("Ingrese un número de teléfono: ")

    
    
    