from sympy import *


def example2():
    x = symbols("x")
    a = cos(x)**2 - sin(x)**2
    b = cos(2*x)
    ret = a.equals(b)
    print("a = ",a)
    print("b = ", b)
    print("a.equals(b) = ", ret)

def example1():
    x = symbols('x')
    a = (x+1)**2
    b = x**2 + 2*x +1
    print("a = ", a)
    print("b = ", b)
    ret = simplify(a - b)
    print("simplify(a-b) = ", ret)
    c = x**2 - 2*x + 1
    ret = simplify (a-c)
    print("simplifiy(a-c) = ", ret)
