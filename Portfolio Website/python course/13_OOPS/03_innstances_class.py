class Employee:
    company = "ASUS" # This is class attributes
    def __init__(self,name,salary,bond,company):
        self.name = name 
        self.salary = salary
        self.bond = bond 
        self.company = company 
    def get_name(self):
        return self.name 
    def get_salary(self):
        return self.salary
    def get_info(self):
        print(f"The Name of the employee is {self.name}. His salary is approx {self.salary}. He has signed the bond for about {self.bond}.He works in {self.company}.  ")     
e1 = Employee("MEET", 80000, 4, "TESLA")
print(e1.get_name())
e1.get_info()
print(e1.get_salary())
print(Employee.company) # The class attribute will always be printed
print(e1.company) # Willl always print instance attribute whenever present


# Object introspection 
print(dir(e1)) #Print sll the methods have in class in Python