def repeat_word(word: str, n: int) -> str:
    return " ".join([word] * n)

def is_even(number: int) -> bool:
    """Verifica si un número es par."""
    return number % 2 == 0

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