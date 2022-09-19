class Person:
    def __int__(self, name):
        self.name = name

    def talk(self):
        print(f'Hi, I am {self.name}')


john = Person()
john.name = "John Smith"
print(john.name)
john.talk()
