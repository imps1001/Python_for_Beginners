# Program to demonstrate conditional operator
a, b = 10, 20
# Copy value of a in min if a < b else copy b
min = a if a < b else b
print(min)

#Nested Ternary Operator 
a=10
b=20
print ("Both a and b are equal" if a == b else "a is greater than b"
        if a > b else "b is greater than a")


x=5
y=7
# [statement_on_True] if [condition] else [statement_on_false]
print(x,"is greater") if (x>y) else print(y,"is Greater")


# Define the data to be evaluated
data = [3, 5, 2, 8, 4]
# Use a for loop to evaluate each element in the data
for num in data:
    # Use the ternary operator to determine if the number is even or odd
    result = 'even' if num % 2 == 0 else 'odd'
    # Optionally, print the result of the ternary operator for each element
    print(f'The number {num} is {result}.')