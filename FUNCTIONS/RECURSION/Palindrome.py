def rev(n,temp):
	if(n==0):
		return temp
	else:
		temp = temp*10 + (n%10)
		return rev(n//10,temp)	



n=int(input("Enter the Number: "))
num = rev(n,0)
if(num==n):
   print(n,"is a palindrome number")
else:      
   print(n,"is not a palindrome")
   
