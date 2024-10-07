#Sean McGaha and Michael Agnew

#Base class animal
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print ("This sound should be set by the subclasses")

    def move(self):
        print(self.name, " is moving")

    def feed(self):
        print("This method should be set by the subclass")

#Derived Class: Monkey (inherits from animal)
class Monkey(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Monkey")

    def make_sound(self):
        print(self.name, " howl")

    def feed(self):
        print(self.name, " eats bananas")

class Snake(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Snake")

    def make_sound(self):
        print(self.name, " Hiss!")

    def feed(self):
        print(self.name, " eats live animals")

class Lion(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Lion")
    
    def make_sound(self):
        print(self.name, " Roars!")
        
    def feed(self):
        print(self.name, " eats gazelles")

class Otter(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Otter")

    def make_sound(self):
        print(self.name, " Whine")

    def feed(self):
        print(self.name, " Eats small fish")

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, " Dog")

    def make_sound(self):
        print(self.name, " Barks")

    def feed(self):
        print(self.name, " Bones")

class Panda(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Panda")

    def make_sound(self):
        print(self.name, " Huffs")

    def feed(self):
        print(self.name, " Eats bamboo")

class Giraffe(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, " Giraffe")

    def make_sound(self):
        print(self.name, " Snorts, Hiss")
    
    def feed(self):
        print(self.name, " Eats Leaves")

class Bear(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, " Bear")

    def make_sound(self):
        print(self.name, " Growls")
    
    def feed(self):
        print(self.name, " Eats fish")






    
