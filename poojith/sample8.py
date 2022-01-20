basicsalary=int(input("enter salary "))
if basicsalary<10000:
    da=((basicsalary*70)/100)
    print ("da",da)
    hra=((basicsalary*65)/100)
    print("hra",hra)
elif 10000>basicsalary<20000:
    da=((basicsalary*75)/100)
    print ("da",da)
    hra=((basicsalary*73)/100)
    print("hra",hra)
else:
    basicsalary>20000
    da=((basicsalary*80)/100)
    print("da",da)
    hra=((basicsalary*76)/100)
    print("hra",hra)
    

    