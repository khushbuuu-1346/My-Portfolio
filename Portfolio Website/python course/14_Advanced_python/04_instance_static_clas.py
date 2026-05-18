class Employee:
      company = "HP"
      def __init__(self,name,salary):
        self.name = name 
        self.salary = salary
      #Instance Method
      def get_info(self):
          return f"The name is {self.name}. And the salary is {self.salary}."
      #Static method 
      @staticmethod
      def sum(a,b):
          c = a+b 
          return c
      #class method
      @classmethod
      def change_company(cls,asus):
          cls.company = asus
          print(cls.company)

e1 = Employee("Jack" , 77987)
e2 = Employee("Jill", 75454)
print(Employee.company)    
print(e1.get_info()) 
print(e2.get_info())  
print(e2.sum(5,6)) 
print(e1.sum(47,47))
e1.change_company("asus")