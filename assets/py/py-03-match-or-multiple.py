def factorial(n):
    match n:
        case -2 | -1 | 0 | 1:
            return 1

        case _:
            return n * factorial(n-1)

print(factorial(-2))
