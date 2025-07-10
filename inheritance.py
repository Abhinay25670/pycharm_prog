class Employee:
    def work(self):
        print("work")
class Manager(Employee):
    def manage(self):
        print("manage")
m1 = Manager()
m2 = Manager()
m1.work()
m1.manage()