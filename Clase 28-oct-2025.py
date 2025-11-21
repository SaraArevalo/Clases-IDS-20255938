palabra = "hola"
#print(len(palabra))
lista = [10, 11, 12, 13, 14]
#print(len(lista))
días = ["Lunes", "Martes", "Miércoles", 
        "Jueves", "Viernes", "Sábado", "Domingo"]
#print(len(días))

#for i in palabra:
    #print(i)
    
"""for i in días[3]:
    print(i)"""
"""
valores = [[1,3,6],
           [2,7,4],
           [6,5,9],
           [1,10,20]]
mayores = []
for v in valores:
    for i in v:
        if i>6:
            mayores.append(i)
print(mayores)
"""
#ejercicio: sacar las veces en las que tiene que pagar horas extra sabiendo que ana
#luis, juan y maria trabajan de lunes a viernes. (hago una lista por días o por nombres)

#while

"""límite = 8
inicio = 0
while inicio < límite:
    print(inicio)
    inicio = inicio + 1"""
    
presupuesto = 1000
gasto = 0
while gasto < presupuesto:
    compra = float(input("Monto a comprar: "))
    gasto += compra
gasto -= compra
print("Ha llegado al límite del presupuesto.")
print(f"El monto gastado es de {gasto:,.2f}")