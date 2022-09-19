class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("Bark")


class Cat(Mammal):
    def meow(self):
        print("Meow")


dog = Dog()
dog.walk()
