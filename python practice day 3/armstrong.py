n=int(input("enter number"))
sum=0
temp=n
while temp>=0:
    digit=temp%10;
    sum +=digit**n;
    temp //=10; 
