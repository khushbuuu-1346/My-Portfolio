class Employee:
    def __init__(self,salary,name,bond):
        self.salary = salary
        self.name = name 
        self.bond = bond 

    def get_salary(self):
        return self.salary
    def get_info(self):
        print(f"The name of the employee is {self.name}. Salary is {self.salary}. With {self.bond} years of bond")
    def get_name(self):
        return self.name
e1 = Employee(3400, "John", 4)
print(e1.get_salary())
e1.get_info()
print(e1.get_name())
