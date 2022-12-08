str1=str(input("enter any string"))


c=input("what you want to do with this string\na) count input string character. \nb)character to replace. \nc)remove first character in string. \nd)remove entire string.\ne) exit \n ****enter your choice in (a/b/c/d)****:- ")
if c=="a" or c=="A":
    a={}
    for i in str1:
      if i in a:
         a[i] +=1
      else:
         a[i]=1
    print(a)
elif c=="b" or c=="B":
    new = str1.replace(input("Enter the character to replace: "), input("Enter the character to replace with: ") )
    print(str1)
    print(new)
elif c=="c" or c=="C":
    l=len(str1)
    print(str1[1:l])

elif c=="d" or c=="D":
    s=str(input("enter any letter from your string to remove:-"))
    print(str1.replace(s,""))

elif c=="e" or c=="E":
    print("thank you for using my code")

else:
    print("enter from (a/b/c/d/e) only")
