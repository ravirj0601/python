s = "abbababababacdegg"
s1 = "a"
pos = -1
s2 = len(s)
for i in range(s2):
    pos = s.find(s1, pos+1, s2)
    if pos != -1:
        print(pos)
    else:
        if pos == -1:
            break
