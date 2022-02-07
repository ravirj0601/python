from typing import Text

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
"""jj=fh.read()
gg=jj.split()
gg.sort()
print(gg)""" 
for line in fh:
    ll=line.split()
    for i in ll:
        lst.append(i)
lst = list(set(lst))
lst.sort()
print(lst)
