n = int(input("Enter a no"))


def diff21(n):
    g = 0
    if n <= 21:
        g = 21-n
        return g
    else:
        g = (n - 21)*2
    return g
print(diff21(n))