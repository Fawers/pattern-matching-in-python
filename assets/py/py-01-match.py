def factorial(n):
    match n:
        case 0:
            return 1

        case 1:
            return 1

        case _:
            return n * factorial(n-1)

print(factorial(5))
