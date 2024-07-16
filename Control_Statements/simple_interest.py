p=int(input("Enter the Principle amount:"))
t=int(input("Enter the time period in Months:"))
r=int(input("Enter the Rate of interest:"))
I=p*t*r/100 
print("Interest is:",I)
print("Total amount with interest:",(p+I))
