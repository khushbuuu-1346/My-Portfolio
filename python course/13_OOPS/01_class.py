class Employee:
    company = "HP"
    def get_salary(self): #self is a way to reference the bject of the class which is being created 
       print(self)
       return 34000

e = Employee() #An object of class Employee is created here
print(e.get_salary())    # Employee e's get salary method is called
e2 = Employee()
print(e2.get_salary()) 
print(e2.company)