a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

operator = str(input("Enter the operator"))
match operator :
    case "+":
        print("Sum= ", a + b)
    case "-":
        print("Difference: ",a - b)
    case "*":
        print("Product: ", a*b)  
    case "/":
        print("Quotient",a/b) 