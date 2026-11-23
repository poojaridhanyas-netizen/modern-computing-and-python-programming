#nested loop
psum=nsum=zerocount=0
num=int(input("enter the number:"))
while(num!=-1):
    if(num>0):
        psum=psum+num
    elif(num<0):
        nsum=nsum+num
    else:
        zerocount=zerocount+1
    num =int(input("enter the number"))
print(f"sum of all positive number:{psum}")
print(f"sum of all negative number:{nsum}")
print(f"count of all zeroes:{zerocount}")

        