import numpy as np

a=eval(input("enter values of row 1"))
b=eval(input("enter values of row 2"))
c=eval(input("enter values of row 3"))
if len(a)==len(b) and len(a)==len(c):
    matrix=np.array([a,b,c])
    print(matrix,"\n this is you matrix")
else:
    print("all must be equal!!!")
