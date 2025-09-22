#EJERCICIO 1

palabra : str = str("Hola mundo!")
print(palabra)

#EJERCICIO 2

nombre : str = str(input("Ingrese su nombre: "))
print(f"Hola {nombre}!")

#EJERCICIO 3

nombre : str = str(input("ingrese su nombre: "))
apellido : str = str(input("ingrese su apellido: "))
edad : int = int(input("ingrese su edad: "))
pais : str = str(input("ingrese su pais: "))
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {pais}")

#EJERCICIO 4

radio : float = float (input("Ingrese el radio del circulo para calcular su área: "))
area : float = 3.14 * radio ** 2
perimetro : float = 2 * radio * 3.14
print(f"el área del círculo es de: {area}")
print(f"el perímetro del círculo es de: {perimetro}")

#EJERCICIO 5

segundos : int = int(input("Ingrese una cantidad de segundos: "))
horas : float = segundos/3600
print(f"{segundos} segundos equivalen a {horas} horas")

#EJERCICIO 6

numero :int = int(input("Ingrese un número para saber su tabla: "))
i : int = int(1)
print(f"La tabla de {numero} es: ")
while i<=10 : 
    resultado: int = numero * i
    print(f"{numero} x {i} = {resultado}")
    i = i+1

#EJERCICIO 7

numero1 : int = int(input("Ingrese un número distinto a 0: "))
numero2 : int = int(input("Ingrese el segundo número distinto a 0: "))
suma: int = numero1 + numero2
resta: int = numero1 - numero2
division: float = numero1/numero2
multiplicacion: int = numero1 * numero2

print(f"La suma de los números es de: {suma}")
print(f"La resta de los números es de: {resta}")
print(f"La división de los números es de: {division}")
print(f"La multiplicación de los números es de: {multiplicacion}")

#EJERCICIO 8

altura : int = int(input("Ingrese su altura: "))
peso : int = int (input("Ingrese su peso: "))
imc : float = altura / peso**2
print(f"Su Indice de Masa Corporal es de: {imc}")

#EJERCICIO 9

grados : float = float(input("Ingrese los grados celsius para convertirlos a grados Fahrenheit: "))
gradosFah : float = (grados * 9/5)+32
print(f"{grados} grados Celsius es equivalente a {gradosFah} grados Fahrenheit")

#EJERCICIO 10

numero1 : int = int(input("Ingrese el primer10 número: "))
numero2 : int = int(input("Ingrese el segundo número: "))
numero3 : int = int(input("Ingrese el tercer número: "))
promedio : float = (numero1 + numero2 + numero3)/ 3
print(f"El promedio de los tres números es de: {promedio}")