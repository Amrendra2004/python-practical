a = input("enter first word:-")
b = input("enter second word:-")
n = int(input("enter number of character you want to replace:-"))
c=a[0:n]
 
a=a.replace(a[0:n],b[0:n])
 
b=b.replace(b[0:n],c)
 
print("your first word is now :- ",a)
print("your second word is now :- ",b)