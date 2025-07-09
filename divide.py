def divide(a,b):
    try:
        div=a/b
        print(int(div))
    except ZeroDivisionError:print("Please enter a valid value for b")
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
divide(a,b)