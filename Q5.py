s=input("Enter a String:-")
s1=len(s)
i=0
for i in range(s1):
    if i % 2 == 0:
        print(s[i],end='')
print()
for i in range(s1):
    if i % 2 != 0:
        print(s[i],end='')

    
        
