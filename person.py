class Person:
    __population = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.__population += 1

    def __str__(self):
        return self.name + ' is ' + str(self.age) + ' years old'

    @classmethod
    def get_population(cls):
        return cls.__population

    @classmethod
    def input(cls):
        name = input('Enter the name: ')
        age = int(input('Enter the age: '))
        return cls(name, age)


print('Currently', Person.get_population(), 'people')
you = Person.input()
print('Now', Person.get_population(), 'person')
actor = Person("Ernie Dingo", 64)
print(actor)
print(you)
print('Now', Person.get_population(), 'people')
