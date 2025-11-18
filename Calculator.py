num1 = int(input("Enter first:"))
num2 = int(input("Enter second:"))

operator= input("Enter operator (+, -, *, /): ")

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2  
elif operator == "/":
    if num2 == 0:
        print("Error: Cannot divide by zero!")
    else:
        result = num1 / num2      
else:
    print("Invalid operator selected")
    
print(f"The result is: {result}")