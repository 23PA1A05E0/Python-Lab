x=input("Enter the String::")
y = ""
l=0
V=['a','e','i','o','u','A','I','O','E','U']
v=0
c=0
for char in x:
    if(char in V ):
        v+=1
    else:
        c+=1    
    y=char+y
    l+=1
print("Original string:",x)    
print("Reversed String:",y)
print("No of Vowels:",v)
print("No of Consonants:",c)
print("Length Of String:",l)  

if(x==y):
    print("Palindrome")
else:
    print("Not a Palindrome")    
