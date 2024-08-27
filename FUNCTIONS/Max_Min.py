def max(l):
	ele=l[0]
	for i in l:
		if(ele<i):
			ele=i
	return ele
def min(l):
	ele=l[0]	
	for i in l:
		if(ele>i):
			ele=i		
	return ele

l=[]
n=int(input("Enter the Size of List"))
for i in range(n):
	ele=int(input())
	l.append(ele)
print(l)			
print("Max=",max(l))
print("Min=",min(l))
