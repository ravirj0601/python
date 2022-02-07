a = int(input("Enter first value:-"))
b = int(input("Enter first value:-"))
c = int(input("Enter first value:-"))
d = int(input("Enter first value:-"))
max = 0
if a > b and a > c and a > d:
    max = a
elif b > c and b > d:
    max = b
elif c > d:
    max = c
else:
    max = d

print("Maximum value is:-",max)
