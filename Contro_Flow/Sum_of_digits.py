n=int(input("Enter the Number: "))
sum =0
num=n
while n!=0:
     ream=n%10
     sum+=ream
     n=n//10
print("Sum of Digits in",num,"is:",sum)     
