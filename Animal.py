class Animal:
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        print("bow bow!!!")
class Cat(Animal):
    def make_sound(self):
        print("meow")
for v in [Dog(), Cat()]:
    v.make_sound()
