class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_age_major(self):
        match self:
            case Person(name=n, age=18):  # 18 é a maioridade na maioria dos países
                print(f'{n} acabou de atingir a maioridade!')
                return True

            case Person(age=a) if a > 18:
                return True

            case _:
                return False


print(Person('Felipe', 18).is_age_major())
print(Person('Fabrício', 29).is_age_major())
print(Person('Letícia', 15).is_age_major())
