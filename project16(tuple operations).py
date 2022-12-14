t1=(1,2,3,4,5,6,7,8,9,10)
t2=(11,13,15)
print("what you want to do with this tuple\n a)split it in half.\n b)print tuple of even numbers.\n c)Concatenate a new tuple.\n d) max. and min. value in tuple. \n e) Exit")
ch=str(input("enter your choice from (a,b,c,d):- "))
if ch=='a' or ch=='A':
      tp=t1[:5]
      tp1=t1[5:]

      print(tp)
      print(tp1)

if ch=='b' or ch=='B':
    for i in t1:
        if i%2==0:
            s.append(i)
    s=tuple(s)
    print(s)
        
if ch=='c' or ch=='C':
    t3=t1+t2
    print(t3)

if ch=='d' or ch=='D':
    t3=t1+t2
    print(max(t3))
    print(min(t3))

if ch=='e' or ch=='E':
    print("thank you")
