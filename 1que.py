
while True:
 x=int(input("enter your marks == "))
 if x >80 :
    print("you got A")
 if x>=61 and x<=80:
    print("you got B")
 if x>=51 and x<=60:
    print("you got C ")
 if x>=46 and x<=50:
    print("you got D")
 if x>=26 and x<=45:
    print("you got E ")
 if x<25 :
    print("you got F")
 check=input("start again ? type Y""\n")
 if check =="Y":
    continue
 else:
   print("thank you visit again")