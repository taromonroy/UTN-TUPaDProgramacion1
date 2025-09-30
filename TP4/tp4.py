"""
EJERCIOCIO 1

"""
for i in range(101):
    print(i)
"""
2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene.

"""
numero = int(input("Ingrese un número entero:"))
digitos = len(str(abs(numero)))
print(f"El número tiene {digitos} digitos")
"""
Ejercicio 3

Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores
"""
numero1 = int(input("Ingrese un número: "))
numero2 = int(input("Ingrese otro número: "))

if numero1 < numero2:
    iniciar = numero1 + 1
    final = numero2
else:
    iniciar = numero2 + 1
    final = numero1
suma = 0
for i in range(iniciar, final):
    print(f"{suma} + {i} = {suma + i}")
    suma += i
print(f"La suma de los números entre {numero1} y {numero2} es de: {suma}")

"""
#### **Ejercicio 4**

Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. 
El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

"""
bandera = True
suma = 0
while bandera:
    numero = int(input(f"ingrese un número para sumar y aprete cero cuando desee finalizar: "))
    if numero == 0:
        bandera = False
    suma += numero

print(f"La suma de los números es de: {suma}")

"""
#### **Ejercicio 5**

Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final,
el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

"""
import random
numeroJuego = random.randint(0,9)
print("Tienes que adivinar un número entre 0 y 9")
intento = 0
bandera = True
while bandera:
    numero = int(input("Ingresa un número: "))
    intento +=1

    if numero == numeroJuego:
        "ADIVINASTE!"
        bandera = False
    elif numero > numeroJuego:
        print("Te pasaste, el número es MENOR. Intentalo de nuevo")
    else:
        print("El número es MENOR. Intentalo de nuevo")

print(f"El número era {numeroJuego} lo lograste en {intento} intentos")

"""
#### **Ejercicio 6**

Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente

"""
print("Números pares de 0 a 100 en orden decreciente")
for i in range(100, -1, 2):
    print(i)

"""
#### **Ejercicio 7**

Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario
"""
numero = int(input("Ingrese un número entero positivo: "))
if numero >= 0:
    suma = 0
    for i in range(numero + 1):
        suma += i
    print(f"La suma de los números entre 0 y {numero} es de {suma}")
else: 
    print("Ingrese un número positivo por favor")

"""
#### **Ejercicio 8**

Escribe un programa que permita al usuario ingresar 100 números enteros.
Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. 
(Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

"""
positivos = 0
negativos = 0
pares = 0
impares = 0

for i in range(5):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    if numero>0:
        positivos += 1
    elif numero<0:
        negativos += 1

    if numero % 2 == 0:
        pares +=1
    else:
        impares+=1

print(f"""
      Hay {positivos} números positivos
      Hay {negativos} números negativos
      Hay {pares} números pares
      Hay {impares} número impares""")

"""
#### **Ejercicio 9**

Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. 
(Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

"""
suma = 0
print(f"Ingrese {100} números enteros: ")
for i in range(100):
    numero = int(input(f"Ingrese el número {i+1}: "))
    suma += numero
media = suma/100

print(f"la media de los números ingresados es {media}")

"""
#### **Ejercicio 10**

Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. 
Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745

"""
numero = int(input("Ingrese un número"))
numero = abs(numero)
numero_invertido = 0
while numero > 0:
    digito = numero % 10 
    numero_invertido = numero_invertido * 10 + digito
    numero //= 10
if numero < 0:
    numero_invertido = -numero_invertido
print(f"El número invertido es: {numero_invertido}")