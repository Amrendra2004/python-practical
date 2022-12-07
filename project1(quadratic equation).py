'''finding roots of quadratic equation by using cmath module
    [ax^2 + bx + c = 0 ]'''

import cmath
a=float(input("enter value of 'a'"))
b=float(input("enter value of 'b'"))
c=float(input("enter value of 'c'"))

# formula to find roots by discriminant  
d = (b**2) - (4*a*c)

#finding solution
x1=(-b-cmath.sqrt(d))/(2*a)
x2=(-b+cmath.sqrt(d))/(2*a)

print("answer of this quadratic equation are {0} and {1}".format(x1,x2))
