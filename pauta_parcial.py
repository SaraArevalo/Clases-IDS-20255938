#Ejercicio 1

num1 = input()
num2 = input()
print(num1 == num2)

#Ejercicio 2

num1 = int(input())
num2 = int(input())
print(num1 // num2 == num1/num2)

#Ejercicio 3

palabra = input()
letra = input()
print(palabra[-1].lower() == letra.lower())

#Ejercicio 4

palabra = input()
print(palabra[::-1].lower() == palabra.lower())

#Ejercicio 5

palabra = input()
letra = input()
print (letra.count(letra) > 0)

#Ejercicio 6

numero = float(input())
print(numero == int(numero))

#Ejercicio 7

dui = input()
cond1 = len(dui) == 10
cond2 = dui[8] == "-"
cond3 = type(dui[-1]) is not float #para comparar TIPOS es is o is not, para comparar VALORES es ==, <=, >=
print(dui)

#o

print(type(int(dui[-1])) is int)
