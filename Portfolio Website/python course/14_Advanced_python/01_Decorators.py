#Decorator is a function that takes a function, it creates a new funtion its body which is wrapper. Then it returns that function
def decorator(func):
    def wrapper():
        print("About to execute the program")
        func()
        print("Executed the program")
    return wrapper()

def say_hello():
    print("Hilllllooooooooo")

decorator(say_hello)
