n = int(input("Enter the number:"))
for i in range(n):
    k = ((n-i+1))
    for j in range(k):
        print(end=" ")
    for j in range(i+1):  
        print(j+1,end=" ")
    for j in range(i,0,-1):
        print(j,end = " ")
    for j in range(k):
        print(end=" ")  
    print()        
        
