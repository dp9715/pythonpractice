p=int(input("enter the price"))
r=int(input("enter the rate"))
t=int(input("enter the time"))
a=p*(pow(1+(r/100),t));
print("final amount is ",a)
c_i=(a-p)
print("compund intrest is ",c_i)