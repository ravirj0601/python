from functools import *
f=lambda a,b:a+b
s=lambda a,b:a-b
m=lambda a,b:a if a>b else b
def main():
    print("For lambda:-     1")
    print("For Filter:-     2")
    print("For Map   :-     3")
    print("For Reduce:-     4")
    print("_______________________")
    n=int(input("Enter Your Choice:- "))
    print()
    if n==1:
        print("----------------------")
        print("For Sum          :- 1")
        print("For substration  :- 2")
        print("For biggest      :- 3")
        print("_______________________")
        d=int(input("Enter your Choice :-"))
        print("----------------------")
        a=int(input("Enter First No:-"))
        b=int(input("Enter second No:-"))
        print("----------------------")
        if d==1:
            print("Sum = ",f(a,b))
        elif d==2:
            print("Subtraction = ",s(a,b))
        else:
            print("biggest No is = ",m(a,b))
    elif n == 2:
        j=eval(input("Enter list Item:-"))
        l=list(filter(lambda x:x%2==0,j))
        l2=list(filter(lambda x:x%2!=0,j))
        print("Even No in the list:-",l)
        print("Odd No in the list :-",l2)
    elif n == 3:
        j=eval(input("Enter First list Item  :-"))
        k=eval(input("Enter Second list Item :-"))
        k1=list(map(lambda x,y:x*y,j,k))
        print("Multiplication of Both List:- ",k1)
    else:
        j=eval(input("Enter a List:- "))
        result=reduce(lambda x,y:x+y,j)
        print(result)

main()


