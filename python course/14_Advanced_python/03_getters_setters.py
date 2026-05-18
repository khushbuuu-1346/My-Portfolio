class MyClass:
    def __init__(self,value):
        self.value = value 
    
    def show(self):
        return (f"Value is {self.value}")
    @property 
    def value_high(self):
        return 10*self.value
    @ten_value.setter
    def ten_value(self,new_value):
     self.value = new_value/10

    
MC = MyClass(10)
print(MC.show())  
print(MC.value_high)
