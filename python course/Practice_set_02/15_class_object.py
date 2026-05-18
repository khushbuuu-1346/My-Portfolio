class Car:
    def drive(self):
        print("Car is moving")
c1= Car()   
c1.drive()     


#problem 2
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
    def get_info(self):
        return f"The name of the person is {self.name}.Also the age is {self.age}. " 
p = person("Khushbu", 20)
print(p.get_info())   

#problem 3   

class Animal:
    
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Bark!")
d = Dog()
d.sound()                
