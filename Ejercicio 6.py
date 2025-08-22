numero :int = int(input("Ingrese un número para saber su tabla: "))
i : int = int(1)
print(f"La tabla de {numero} es: ")
while i<=10 : 
    resultado: int = numero * i
    print(f"{numero} x {i} = {resultado}")
    i = i+1