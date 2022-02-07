fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
kk=list()
fh = open(fname)
count = 0
for line in fh:
    kk=line.split()
    if len(kk) < 1 or kk[0] != 'From':
        continue
    count+=1
    print(kk[1])


print("There were", count, "lines in the file with From as the first word")