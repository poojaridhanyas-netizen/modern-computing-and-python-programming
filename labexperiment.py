#to read 3 values and find the largest amon them
a=int(input("enter the value for a:"))
b=int(input("enter the value for b:"))
c=int(input("enter the value for c:"))
if (a>b and a>c) :
    print(f"{a} is largest")
elif (b>a and b>c) :
    print(f"{b} is largest")
else:
    print(f"{c} is largest")