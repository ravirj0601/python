s1=input("Enter an String:-")
s2=input("Enter an String:-")
l1=len(s1)
l2=len(s2)

i=0
j=0
l=[]
while l1>i and l2>j:
    l.append(s1[i])
    l.append(s2[j])
    i=i+1
    j=j+1

while l1>i:
    l.append(s1[i])
    i=i+1

while l2>j:
    l.append(s2[j])
    j=j+1
output=''.join(l)
print(output)