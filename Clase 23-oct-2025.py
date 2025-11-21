#if anidado

"""monto = float(input("Digite el monto: "))
tipo = input("Tipo (local/internacional): ")
impuesto = 0

if tipo.lower() == "local":
    if monto > 100:
        impuesto = 0.07
    else: 
        if monto > 75:
            impuesto = 0.05
        else: 
            impuesto = 0
            
elif tipo.lower() == "internacional":
    if monto > 100:
        impuesto = 0.12
    else:
        if monto > 75: #esta parte también se puede poner como un "elif".
            impuesto = 0.09
        else:
            impuesto = 0

else:
    print ("Ese tipo no existe.")
print(f"El tipo {tipo} con monto {monto:,.2f}")
print(f"paga un impuesto de {monto*impuesto:,.2f}")"""

#for_s2

nombres = ["Ana", "José", "Luis"] #se está asignando "x" a cada valor de la lista; es decir, que los tres nombres se consideran "x".
for x in nombres:
    print("Hola") #para cada iterador en el que pueda proceder, haga algo. En este caso, imprima "hola" por cada iterador con el valor "x".

for i in nombres:
    if i == "José":
        print ("Lo encontré.")
    else:
        print ("No está José.")