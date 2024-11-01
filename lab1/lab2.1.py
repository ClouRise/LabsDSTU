from math import sin, cos
from numpy import arange

x0 = (input("введите X0  "))
x1 = (input("введите X1  "))
dx = (input("введите значение шага  "))
try:
    x0 = float(x0)
except(ValueError):
      print("x0 должно быть числом")
else:
    try:
        x1 = float(x1)
    except(ValueError):
        print("x1 должно быть числом")
    else:
        try:
            dx = float(dx)
        except(ValueError):
            print("dx должно быть числом")
        else:
            z = 0
            for x in arange(x0,x1+dx,dx):
                if x<0: z = x*x
                elif (x>0)and(x<=1): z = sin(x)
                else: z = cos(x)
                print("z =", z)  