# define a new type 'Person'
# should have 'name' attribute
# and 'talk()' method

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hola, my name is {self.name}")


john = Person("John Patrick")
john.talk()

bob = Person("Bob Vance, Vance Refrigeration")
bob.talk()

# pre ano to
