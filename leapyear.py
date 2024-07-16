a=int(input("Enter the Year::"))

if((a%4==0 and a%100!=0) or (a%400==0)):
  print(a,"is Leap year")
  
else:
  print(a,"is non Leap year")
    
