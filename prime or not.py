num= int(input("enter the number :" ))
count=0
i=1
while i<=num:
    if num%i==0:
        count+=1
        i+=1
        

if count==2:
    print("number is the prime")
                
else:
        print("number is not prime")



