def divide(a,b):
   try:
      c = a/b 
      print(c)
   except Exception as e:
     print(e) 
   finally:
    print("This will always executed")    
a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
divide(a,b)   