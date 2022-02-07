def ex_decor1():
    def hh(func):
        def inner(name):
            if name == "Ravi":
                print("You are awesome Ravi.")
            else:
                func(name)
        return inner
    @hh
    def wish(name):
        print("Hello you are awesome Too",name)

def nested_fun():
    a=4
    b=5
    def fun1(a,b):
        print("Outer")
        def fun2(a,b):
            s=a+b
            print("sum:-",s)
        print("Calling Inner")
        return fun2
    fun1(a,b)

def ex_decor():
    def decor(func):
        def some(a,b):
            print("We are dividing",a,"With",b)
            if b == 0:
                print("Can't Divide")
                return
            else:
                return func(a,b)
        return some
    @decor
    def devide(a,b):
        print(a/b)
        #return a/b
    a=int(input("Enter First No:- "))
    b=int(input("Enter First No:- "))
    devide(a,b)

array=set()
array={161,182,161,154,176,170,167,171,170,174}
def average(array):
    count=0
    sum=0
    for i in array:
        sum+=i
        count+=1
    ave=sum/count
    print(ave)

average(array)