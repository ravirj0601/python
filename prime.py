n=23    #int(input("Enter a No:-"))
p=True
for i in range(0,n):
    if n % i == 0:
        p=False
        break
if p==True:
    print("Prime")
else:
    print("Not Prime")
