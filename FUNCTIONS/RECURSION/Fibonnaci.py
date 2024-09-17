def fibb(n):
	if n<=1:
		return n
	else:
		return fibb(n-1) + fibb(n-2)
n= int(input("Enter the Number:"))
print("Fibonacci Series:",end='  ')
for i in range(n):
	print(fibb(i),end = ' ')
				
print("")	
