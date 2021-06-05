def exhaustive_matching(number):
    match number:
        case -1:
            return '<'

        case 0:
            return '='

        case 1:
            return '>'

        case _:
            return 'dunno'


def non_exhaustive_matching(number):
    match number:
        case -1:
            return '<'

        case 0:
            return '='

        case 1:
            return '>'


print(exhaustive_matching(10))
print(non_exhaustive_matching(-10))
