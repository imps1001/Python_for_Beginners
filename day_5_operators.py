# # Arithmetic Operators
# print(5+15)
# print(15-5)
# print(4*5)
# print(61/2)
# print(3**4)
# print(43//2)

# #Comparison Operators

# print(5>3) #true
# print(4<3) #false
# print(30>=9) #true
# print(89<=90) #true
# print(89==56) #false
# print(56!=90) #true

# #Logical Operators
# print(5>3 and 3>4) #true and false => false
# print(45==90 or 34<90) #fase or true => true
# print(not 54>89) #not false => true

# #Assignment Operators
# x=5
# print(x)
# x+=4 # x=x+4 => x=9
# print(x) #9
# x-=3 # x=9-3 => 6
# print(x) #6
# x*=5 # x=6*5 => 30
# print(x) #30

# #Identity Operators 
# x = ["abcd", "ball"]
# y = ["abcd", "ball"]
# z = x
# print(x is z) #true
# print(x is y) #false
# print(x==y) #true

# #Membership Operators
x = ["abcd", "ball"]

print("ball" in x) #true
print("abcd" not in x) #false


# #Operator precedence 
print((7 + 5) - (7 + 5)) #0
print(100 + 5 * 3) #115
print(5 + 4 - 7 + 3)  #5
"""
Additions and subtractions have the same precedence, and we need to calculate from left to right.
The calculation above reads:
5 + 4 = 9
9 - 7 = 2
2 + 3 = 5
"""
a=18
print(~a)
