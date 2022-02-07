'''name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt" '''''

handle = open('mbox-short.txt')
kk=dict()
for line in handle:
    words = line.split()
    if len(words) < 1 or words[0] != 'From':
        continue
    words = line.split()
    ff=words[1]
    kk[ff]=kk.get(ff,0)+1
print(kk)
bigcount = None
bigword = None
for ff,count in kk.items():
    if bigcount is None or count > bigcount:
        bigword = ff
        bigcount = count
print(bigword, bigcount,)


