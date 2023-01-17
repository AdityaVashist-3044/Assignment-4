x=int(input("Enter the year""\n"))
if (x%4==0 and x%100 !=0) or (x%400==0):
    print(x,"this is a leap year") 
   
else :
    print(x,"is not a leap year ")