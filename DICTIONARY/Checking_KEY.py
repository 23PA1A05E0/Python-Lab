d = {1 :10, 2:20 ,3:30 ,4:40}
l = list(d.keys())
print(l)
n = int(input("Enter the key to check:"))
flag =-1
for i in l:
	if i==n:
		pos = i
		flag = 1
		break
if(flag == 1):
	print("Key Exists")
else:
	print("Key doesn't exists")		
