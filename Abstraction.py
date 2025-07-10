from abc import ABC, abstractmethod
class Abstraction(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
class UPI (Abstraction):
    def pay(self,amount):
        print(amount)
a = UPI()
a.pay(10000)