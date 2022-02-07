name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
th = dict()
for line in handle:
    dd = line.split()
    if len(dd) < 1 or  dd[0] != 'From':
        continue
    ff=dd[5].split(':')
    jj=ff[0]
    th[jj]=th.get(jj,0)+1
for jj,count in sorted(th.items()):
    print(jj,count)


    
    
    