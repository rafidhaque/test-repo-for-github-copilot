def reverse_string(value: str) -> str:
    return value[::-1]


def is_prime(value: int) -> bool:
    if value < 2:
        return False

    for divisor in range(2, int(value**0.5) + 1):
        if value % divisor == 0:
            return False

    return True
