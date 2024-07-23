n=int(input("Enter the Number: "))
sum =0
org=n
num=0
while n!=0:
     ream=n%10
     num=(num*10)+ream
     n=n//10

print("The Reverse of number",org,"s:",num)
