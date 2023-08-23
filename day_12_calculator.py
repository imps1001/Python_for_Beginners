#Create a calculator in which user will tell us the operation and the operands to perform the operation.
# Our Calculator can perform addition, subtraction, multiplication, division and modulus.
"""
Example : 
Enter the operation -
1 for Addition
2 for Subtraction
3 for Multiply
4 for Division
5 for Modulus

Input - 1
Enter the values : 4 5
Output : 9
"""










print("Enter 1 for Addition \n2 for Subtraction \n3 for Multiply \n4 for Division \n5 for Modulus\n")
operation = int(input("Tell the type of operation - "))
a, b = map(int, input("Enter the Numbers: ").split())

try:
        if operation == 1:
            result = a + b
        elif operation == 2:
            result = a - b
        elif operation == 3:
            result = a * b
        elif operation == 4:
            result = a / b
        elif operation == 5:
            result = a % b
        else:
            print("Invalid operation")

        print("Result:", result)

except ZeroDivisionError:
        print("Error: Division by zero not allowed.")