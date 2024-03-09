def start():
    a = int(input("Enter a number"))
    b = int(input("Enter a number"))
    sum = add(a,b)
    average = avg(a,b)
    power = exponent(a,b)
    print("Sum is",sum)
    print("Average is", average)
    print("Power is", power)


def add(a,b):
    return a+b

def avg(a,b):
    average = (a+b)/2
    return average

def exponent(a,b):
    return a**b

if __name__=='__main__':
    start()