n=int(input("Enter a number to check perfect number or not:"))
sum=0
for i in range(1,n):
      if(n%i==0):
      	  sum+=i
if(n==sum):
      print(n,"Is a Perfect Number")
else:
      print(n,"is not a Perfect Number")            	  
