l=[]
n=int(input("Enter the No.of Element:"))
for i in range(n):
	ele=int(input("Enter the element:"))
	l.append(ele)
print(l)
print("Sum of List is",sum(l))
print("Average of List",(sum(l)/len(l)))	
