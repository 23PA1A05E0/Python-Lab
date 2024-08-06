l=[]
n=int(input("Enter the No.of Element:"))
for i in range(n):
	ele=int(input("Enter the element:"))
	l.append(ele)
print(l)
print("Interchaing Firse and Last elment:")
temp=l[0]
l[0]=l[-1]
l[-1]=temp
print(l)
