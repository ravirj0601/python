s = input("enter a String:-")
l = s.split()
s1 = len(l)
for i in l:
    if s1 != -1:
        print(l[s1-1], end=' ')
    s1 = s1-1
