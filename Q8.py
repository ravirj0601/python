def getFact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*getFact(n-1)

print(getFact(4))