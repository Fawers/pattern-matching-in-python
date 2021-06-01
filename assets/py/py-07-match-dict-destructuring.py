def match_dict(the_dict):
    match the_dict:
        case _ if len(the_dict) == 0:
            print('o dicionário está vazio')

        case {'name': nome}:
            print(f'a chave nome possui o valor {nome}')

        case {'date': data, 'article': {'title': titulo}}:
            print(f'o artigo {titulo} foi publicado em {data}')

        case _:
            print('nenhuma chave nos interessa')

match_dict({})
match_dict({'name': 'Fabricio', 'age': 29})
match_dict({'date': '31/05/2021', 'time': '20:49', 'article': {'title': 'Pattern Matching do Python'}})
match_dict({'what is love': "baby don't hurt me"})
