amount=int(input("enter amount"))
a=0
b=0
c=0
d=0
e=0
if amount%10==0:
    if amount>=200:
        a=amount//200
        amount=amount-(200*a)
        print("200 rupees notes are")
    if amount>=100:
        a=amount//100
        amount=amount-(100*b)
        print("100 rupees notes are")
    if    amount>=50:
        a=amount//50
        amount=amount-(50*c)
        print("50 rupees notes are")  
    if    amount>=20:
        a=amount//20
        amount=amount-(20*d)
        print("20 rupees notes are")
    if   amount>=10:
        a=amount//10
        amount=amount-(10*e)
        print("10 rupees notes are")    
else:
    print("unable to withdraw the enterd amount")
    