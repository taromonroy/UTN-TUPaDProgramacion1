"""EJERCICIO 1"""
def es_numero_positivo(mensaje):
    while True:
        numero = input(mensaje)
        if numero.isdigit():
            numero = int(numero)
            if numero < 1:
                print ("El numero debe ser mayor o igual a 1")
                continue
            else:
                return numero
        print("numero no admitido")

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)

def main():
    maximo = es_numero_positivo("ingrese un numero positivo y mayor a 1: ")
    minimo = 1
    for minimo in range(1,maximo+1):
        print(f"El factorial {minimo} es: {factorial(minimo)}")

main()

"""EJERCICIO 2"""
def es_numero_positivo(mensaje):
    while True:
        numero = input(mensaje)
        if numero.isdigit():
            numero = int(numero)
            if numero < 1:
                print ("El numero debe ser mayor o igual a 1")
                continue
            else:
                return numero
        print("numero no admitido")

def serie_fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return serie_fibonacci(num -1) + serie_fibonacci(num - 2)

def main():
    indice = es_numero_positivo("ingrese la posicion donde quiere efectuar la serie de Fibonacci: ")
    print("Serie Fibonacci: ")
    for i in range(indice+1):
        print(f"{i}: {serie_fibonacci(i)}")

main()

"""EJERCICIO 3"""
def es_numero_positivo(mensaje):
    while True:
        numero = input(mensaje)
        if numero.isdigit():
            numero = int(numero)
            if numero < 1:
                print ("El numero debe ser mayor o igual a 1")
                continue
            else:
                return numero
        print("numero no admitido")

def potencia_recursiva(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia_recursiva(base, exponente - 1)

def main():
    exponente = es_numero_positivo("ingrese un exponente: ")
    base = es_numero_positivo("ingrese una base: ")
    resultado = potencia_recursiva(base,exponente)
    print("El resultado de la formula es: ",resultado)

main()

"""EJERCICIO 4"""
def es_numero_positivo(mensaje):
    while True:
        numero = input(mensaje)
        if numero.isdigit():
            numero = int(numero)
            if numero < 1:
                print ("El numero debe ser mayor o igual a 1")
                continue
            else:
                return numero
        print("numero no admitido")

def decimal_a_binario(num):
    if num < 2:
        return str(num)
    else:
        return decimal_a_binario(num // 2) + str(num % 2)

def main():
    numero = es_numero_positivo("ingrese un numero: ")
    print(f"Decimal {numero} | Binario: {decimal_a_binario(numero)}")

main()

"""EJERCICIO 5"""
def palabra_modificada(palabra):
    return ''.join(palabra.lower().strip().split())

def es_palindromo(palabra):
    palabra = palabra_modificada(palabra)
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

def main():
    palabra = input("ingrese una palabra para determinar si es palindromo: ")

    if es_palindromo(palabra):
        print("La palabra es un palindromo")
    else:
        print("La palabra no es un palindromo")

main()
"""EJERCICIO 6"""
def es_numero_positivo(mensaje):
    while True:
        numero = input(mensaje)
        if numero.isdigit():
            numero = int(numero)
            return numero
        print("numero no admitido")

def suma_digitos(n):
    if n < 10:
        return n
    else:
        ultimo_digito = n % 10
        resto = n // 10
        return ultimo_digito + suma_digitos(resto)

digito = suma_digitos(es_numero_positivo("ingrese un numero positivo y entero: "))

print("La suma de los digitos es: ",digito)

"""EJERCICIO 7"""
def es_numero_positivo(mensaje):
    while True:
        numero = input(mensaje)
        if numero.isdigit():
            numero = int(numero)
            if numero < 1:
                print ("El numero debe ser mayor o igual a 1")
                continue
            else:
                return numero
        print("numero no admitido")

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

numero = contar_bloques(es_numero_positivo("ingrese un numero mayor a 0: "))

print("La suma de los numeros : ",numero)

"""EJERCICIO 8"""
def es_numero_positivo(mensaje):
    while True:
        numero = input(mensaje)
        if numero.isdigit():
            numero = int(numero)
            return numero
        print("numero no admitido")

def contar_digito(numero, digito):
    if numero < 10:
        if numero == digito:
            return 1
        else:
            return 0
    else:
        ultimo_digito = numero % 10
        
        if ultimo_digito == digito:
            cuenta_actual = 1
        else:
            cuenta_actual = 0
        
        resto = numero // 10
        return cuenta_actual + contar_digito(resto, digito)

numero = es_numero_positivo("ingrese un numero positivo: ")

digito = es_numero_positivo("ingrese un digito entre 0-9: ")

while True:
    if digito > 9:
        digito = es_numero_positivo("numero no admitido, pruebe nuevamente entre 0-9: ")
    else:
        break

repetidos = contar_digito(numero, digito)