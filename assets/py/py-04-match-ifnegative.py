def factorial(n):
    match n:
        case 0 | 1:
            return 1

        case _:
            return None if n < 0 else n * factorial(n-1)
            # ou
            if n < 0:
                return None

            else:
                return n * factorial(n-1)

print(factorial(-1))
