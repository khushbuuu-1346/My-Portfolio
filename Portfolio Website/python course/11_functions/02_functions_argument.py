def add(a,b):
    return a+b 
c = add(3,4)
print(c)

def add(a,b,plus=0):
    return a + b + plus
c = add(36,4,34)
print(c)

c1 = add(b=3,a=5)
print(c1)
#default arguments 
def greet(name = "Guest"):
    return f"Hello,{name}"
print(greet())

def student(name , age):
    print(f"Name:{name},Age : {age}")
student("Khushbu",20)   

def student(Name,Age):
    print(f"Name:{Name} Age:{Age}")
student("Khushbu",20)    