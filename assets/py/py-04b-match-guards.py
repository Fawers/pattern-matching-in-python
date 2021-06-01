def factorial(n):
    match n:
        case 0 | 1:
            return 1

        case _ if n > 1:
            return n * factorial(n-1)

        case _:
            return None

print(factorial(-3))
