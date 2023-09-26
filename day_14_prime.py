# Prime Number Program
# A number that can be divided exactly only by itself and 1, for example 7, 17 and 41

# Programs Covered
# 1. Program to check a number is prime or not?
# 2. Program to print prime numbers between a to b.

n= int(input("Enter a no"))
c=0
for i in range(2,n):
    if(n%i==0):
        c=c+1
if(c==0):
    print("Number is prime")
else:
    print("Number is not prime")

a= int(input("Enter a no"))
b= int(input("Enter a no"))
for n in range(a,b+1):
    c=0
    for i in range(2, n):
        if(n%i==0):
            c= c+1
    if(c==0):
        print(n)
