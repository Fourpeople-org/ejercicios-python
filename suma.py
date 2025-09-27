# Programa que pide dos números y muestra su suma

try:
    # Pedir los números al usuario
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))

    # Sumar los números
    c = a + b

    # Mostrar el resultado
    print(f"La suma de {a} y {b} es igual a: {c}")

except ValueError:
    print("Error: Debes ingresar solo números enteros.")
