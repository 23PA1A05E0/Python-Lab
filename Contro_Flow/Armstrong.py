n=int(input("Enter the Number: "))
i=0
num=n
while n!=0:
     ream=n%10
     i=i+1
     n=n//10

ream=0
arm=0
n=num
while num!=0:
     ream=num%10
     arm=arm+(ream**i) 
     num=num//10
if(arm==n):
      print(n,"is a Armstrong Number")
   
else:
      print(n,"is not a Armstrong Number")        
