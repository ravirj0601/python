a=int(input("enter a Value"))
b=int(input("enter a Value"))

def sum_double(a, b):
    if a == b:
        return (a+b)*2
    else:
        return a + b

print(sum_double(a,b))