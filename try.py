from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def is_adult(age):
        return age > 18


person1 = Person('gab', 21)
person2 = Person.from_birth_year('gab', 1996)

print(person1.age)
