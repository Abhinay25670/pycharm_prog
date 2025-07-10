class Product:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.__balance=0
    def print_details(self):
        print(self.name,self.age)
    def get_balance(self):
        return self.__balance
    def set_balance(self,balance):
        self.__balance+=balance
p1=Product("David",10)
p2=Product("Harry",20)
p1.print_details()
p2.print_details()
print(p1.get_balance())
p1.set_balance(100000)
print(p1.get_balance())
