def max (l):
	ele=l[0]
	for i in l:
		if(ele<i):
			sec=ele
			ele=i		
	return sec

l=[]
n=int(input("Enter the Size of List"))
for i in range(n):
	ele=int(input())
	l.append(ele)
print(l)			
print("Max=",max(l))
