#String & Character literals
# in single quote
a = 'learning Code'

# in double quotes
b = "learning Code"

# multi-line String
c = '''Code
            At
               random'''

print(a)
print(b)
print(c)


#Numeric Literal - Integer, Float, Complex
# integer literal
# Binary Literals
a = 0b10100
# Decimal Literal
b = 50
# Octal Literal
c = 0o320
# Hexadecimal Literal
d = 0x12b
print(a, b, c, d)


# Float Literal
e = 24.8
f = 45.0
print(e, f)

#Complex Literal
z = 7 + 5j
k = 7j # real part is 0 here.
print(z, k)

#Boolean Literal - True =1 and False =0
a = (1 == True)
b = (1 == False)
c = True + 3
d = False + 7
print("a is", a)
print("b is", b)
print("c:", c)
print("d:", d)


#Literal Collection - List, Tuple, Dict, Set
#List
number = [1, 2, 3, 4, 5]
name = ['Amit', 'kabir', 'bhaskar', 2,89.7]
print(number)
print(name)

#tuple
even_number = (2, 4, 6, 8,2)
odd_number = (1, 3, 5, 7)
print(even_number)
print(odd_number)

#dict
alphabets = {'a': 'apple', 'b': 'ball', 'c': 'cat'}
information = {'name': 'amit', 'age': 20, 'ID': 20}
print(alphabets)
print(information)

#Set Literal
vowels = {'a', 'e', 'i', 'o', 'u'}
fruits = {"apple", "banana", "cherry"}
print(vowels)
print(fruits)


#Special Literal - None
water_remain = None
print(water_remain)