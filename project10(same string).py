
a=str(input("enter any first string"))
b=str(input("enter any second string"))
c=list(a)
d=list(b)
for i in d:
  if i in c:
    c.append(i)
print(c)

    