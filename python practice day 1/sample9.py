n1=int(input("enter number"))
n2=int(input("enter number"))
n3=int(input("enter number"))
print("given numbers are",n1,n2,n3);
if (n1>n2)&(n1>n3):
    print("n1",n1)
elif (n2>n1)&(n2>n3):
    print("n2",n2)
else:
    print("n3",n3)
