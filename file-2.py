fname = input("Enter file name: ")
fh = open(fname)
sum=0
count=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count=count+1
    y=line.find(':')
    x=len(line)
    z=line[x-7:x]
    h=float(z)
    sum=h+sum

print('average spam confidence: ',sum/count)

    