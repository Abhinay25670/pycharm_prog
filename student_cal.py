import logic as l

name=input("Enter your name: ")
rollno=input("Enter your rollno: ")
marks=list(map(int,input("Enter your python marks: ").split()))
print(marks)
avg=int(l.average(marks))
print("Your Average:",avg)
print("Your Grade:",l.grade(avg))


