n=int(input("Enter the Number Of Rows::"))
 
for i in range(0,n+1):
	for j in range(0,n+i):
		if(j<n-i-1):
			print(" ",sep="\t",end="")
		else:
			print("*",sep="\t",end="")
	print("\n")			
