age = int(input("Enter the age: "))
if(age>=18):
    print("You can vote")
elif(age==18):
    print("You are eligible")
elif(age==0):
    print("Just born") 
else:
    print("You can not vote")  



marks = int(input("Enter your marks : ")) 
if(marks<=20):
    print("Fail")
elif((marks>=20) & (marks<=80)):
    print("Pass")
    print("With  average grades")
else:
    print("Pass with A grade")    


num  = int(input("Enter a number : "))
if(num%2==0):
    print("Number is even")
else:   
    print("Number is odd") 
