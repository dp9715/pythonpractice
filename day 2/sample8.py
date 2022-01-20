n=int(input("enter number "))
if n>1:
    
    for i in range(2,n):
        if(n%i==0):
            print ("its not a prime number")
            break;
    else:
        
        print("given number is prime")
else:
    if n==1:
        print("its not prime number")
        
            
        
    
    
    

    