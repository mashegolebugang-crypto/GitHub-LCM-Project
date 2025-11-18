print("=== even or odd checker")

try:
    number = int(input("enter an integer: "))
    
    if number % 2 == 0:
        print(number, "is even.")
    else:
        print(number, "is odd.")
except ValueError:
    print("error: please enter a valid interger!")