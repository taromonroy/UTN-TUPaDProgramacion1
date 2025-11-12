"""
EJERCICIO 1

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

"""

"""
EJERCICIO 2

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre = input("Ingrese su nombre: ")
saludo = saludar_usuario(nombre)
print(saludo)

"""
"""
EJERCICIO 3

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

"""
"""
EJERCICIO 4



"""
PI = 3.14

def calcular_area_circulo(radio):
    return PI * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * PI * radio

radio = float(input("Ingrese el radio del círculo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")