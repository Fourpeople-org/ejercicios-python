def repeat_word(word: str, n: int) -> str:
    return " ".join([word] * n)

try:
    # Pedir los números al usuario
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))

    # Sumar los números
    c = a + b

    # Mostrar el resultado
    print(f"La suma de {a} y {b} es igual a: {c}")

except ValueError: