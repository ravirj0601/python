
def ent_dict():
    d=eval(input("Enter dictionary:"))
    s=sum(d.values())
    print("sum=",s)

def occur_ce(w):
    d=dict()
    for i in w:
        d[i]=d.get(i,0)+1
    for i,v in d.items():
        print("keys:-",i,"and occurance :-",v)

def prime(num):
    p=True
    for i in range(0,num):
        if n % i == 0:
            p=False
            break
    if p==True:
        print("Prime")
    else:
        print("Not Prime")

def fact(num):
    result=1
    while num>=1:
        result *= num
        num -= 1
    print(result)
    return 0

def add(a,b):
    s=a+b
    print(s)
    return 0
def multi(a,b):
    m=a*b
    print(m)
    return a*b
def substration(a,b):
    if a>b:
        m= a-b
        print(m)
    else:
        m= b-a
        print(m)
def div(a,b):
    divs=a/b
    print(divs)
    return 0


def main(n):
   
    if n == 1:
        print("For Factorial        :- 1")
        a=int(input("Enter a No:- "))
        operation(a)
    else:
        print("For Division         :- 1 ")
        print("For Addition         :- 2 ")
        print("For Substration      :- 3 ")
        print("For Multiplication   :- 4 ")
        num=int(input("Enter Your Choice :- "))
        a=int(input("Enter First No:- "))
        b=int(input("Enter First No:- "))
        c=cal(num,a,b)
        print(c)

def operation(a):
   fact(a)
       
def cal(x,a,b):
   
    switcher = {   
        1:div(a,b),
        2:add(a,b),
        3:substration(a,b),
        4:multi(a,b),
        
    }
    return switcher.get(x,"option not available")

print("For Operations       :- 1")
print("For Calculator       :- 2")
n=int(input("Enter your choice:-"))

main(n)    
    

    
    
'''else:
    g=int(input("Enter First No:-"))
    h=int(input("Enter First No:-"))'''

#c=cal(n,g,h)
#print(c)


