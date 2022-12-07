a=input("do you want positive or nagative pyramid from(+/-)")
if a=="+":
   n= int(input("enter number of rows:-"))
   b=int(1)
   while n!=0:
     print("*"*b,"\n")
     b+=2
     n -= 1
elif a=="-":
    n= int(input("enter number of rows:-"))
    b=int(1)
    while n!=0:
     print("*"*(2*n-1))
     n -= 1
else:
    print("enter correct number")
    