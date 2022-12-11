a = open('text.txt','r')
b = open('file1.txt','w')
c = open('file2.txt','w')
d=a.readlines()
for i in d:
    s=d.index(i)
    t=s+1
    if t%2==0:
        b.write(i)
    else:
        c.write(i)
