# A SMALL PROJECT THAT WORK LIKE A SMALL CALCULATOR:

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def avg(a,b):
    return (a+b)/2

num1 = int(input("Enter first number:"))
sym = input("Enter symbol:")
num2 = int(input("Enter second number:"))

if sym=="+":
    n =add(num1,num2)
    print(f"{num1} + {num2} = ",n)

elif sym=="-":
    n = sub(num1,num2)
    print(f"{num1} - {num2} = ",n)

elif sym == "/":
    n = div(num1/num2)
    print(f"{num1} / {num2} = ",n)

elif sym =="*":
    n = mul(num1,num2)
    print(f"{num1} * {num2} = ",n)

elif sym == "avg":
    n = avg(num1,num2)
    print(f"The average of {num1} and {num2} is : ",n)

else:
    print("Currently i am unable to do this.'SORRY!'")