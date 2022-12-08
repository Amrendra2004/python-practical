#list of cube of only even numbers.
a=eval(input("enter any list of numbers:-"))
s=[]
for i in a:
    if i%2==0:
        s.append(i**3)
print(s)