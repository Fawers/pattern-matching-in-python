def match_list(the_list):
    match the_list:
        case []:
            print('a lista está vazia')

        case [x]:
            print(f'a lista possui um único elemento: {x}')

        case [x, y]:
            print(f'a lista possui dois elementos: {x} e {y}')

        case _:
            print('a lista possui mais de dois elementos')

match_list([])
match_list([10])
match_list([3, 7])
match_list([1, 2, 3, 4, 5])
