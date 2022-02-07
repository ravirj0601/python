stu=int(input("Enter a no of studnt:- "))
d=dict()
for n in range(stu):
    name=input("input Name of the Student:- ")
    marks=int(input("Input Marks of the student:- "))
    d[name]=marks 
print(d)
while True:
    name=input("Enter a name of the student you want to knoe the marks:-")
    marks=d.get(name,-1)
  
    if marks==-1:
        print("student not found")
    else:
        print(name,marks)
    option=input("Go further?[yes/no]")
    if option=="no": 
        break
