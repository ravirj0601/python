for i in range(10):
    if i%2==0:
        continue
    print(i)
print()


####################################################


cart = [10,20,400,500,63,10]   
for item in cart:
    if item >= 500:
        print("Already have Enough!")
        continue
    print(item)


####################################################


no = [10,20,0,5,0,30]
for n in no:
    if n==0:
        print("it can't be divisible by 0")
        continue
    s=n*10
    print(s)
