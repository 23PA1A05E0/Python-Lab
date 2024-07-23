n=int(input("Enter the Number: "))
flag=0
num=n
n=n//2
for i in range(2,n):
     if(num%i==0):
        flag=1
        break;
     flag=flag+1
        
if(flag==1):
   print(num,"is not a prime Number")
else:
   print(num,"is a Prime Number")              
