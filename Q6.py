s=input("enter First string:-")
l=s.split()
sl=len(l)
s1=''
s2=''
i=0
for i in s:
    if i.isalpha():
        s1=s1+i
    else:
        s2=s2+i
print(sorted(s1))
print(sorted(s2))
