class Vehicle:
    def navigate(self):
        pass
class Car(Vehicle):
    def navigate(self):
        print("navigate via car")


class Truck(Vehicle):
    def navigate(self):
        print("navigate via truck")
c1=Car()
c1.navigate()