"""
Program to print the kinetic enegry of a moving body whose mass and velocity will be input by the user.

Kinetic Energy = ½ mv2
"""
m = int(input("Enter mass"))
v = int(input("Enter velocity"))
ke = 0.5 * (m*v*v)
print(ke)