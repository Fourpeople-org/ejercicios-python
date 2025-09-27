def repeat_word(word: str, n: int) -> str:
    return " ".join([word] * n)

def is_even(number: int) -> bool:
    """Verifica si un número es par."""
    return number % 2 == 0