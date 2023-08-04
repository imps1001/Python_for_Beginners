# # Taking input from the user
name = input("Enter your name")
print(name)

# # Taking input from the user as integer
num = int(input("Enter a number"))
print(type(num))

# #Taking multiple inputs from the user
a, b, c = map(int, input("Enter the Numbers : ").split())
print("The Numbers are : ",end = " ")
print(a, b, c)

# #Taking Input using map() and list() / set() method
List = list(map(str, input("Enter List elements : ").split()))
Set = set(map(int, input("Enter the Set elements :").split()))
print(List)
print(Set)




#Example 1
# print() method
print("C@R")
print('C', 'O', 'D', 'E')
print("a")


# #Example 2
print("C@R", end = "#")
# # code for disabling the softspace feature 
print('C', 'O', 'D', 'E',  sep="@")
