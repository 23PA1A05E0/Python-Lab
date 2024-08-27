def gcd_fun(a,b):
	if(b==0):
		return a
	else:
		return gcd_fun(b,a%b)
a=int(input("Enter the first number:"))		
b=int(input("Enter the Second number:"))
print("GCD of",a,b,"is:",gcd_fun(a,b))			
