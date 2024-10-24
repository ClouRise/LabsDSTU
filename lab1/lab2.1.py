from math import sin, cos

x0 = int(input("введите X0  "))
x1 = int(input("введите X1  "))
dx = int(input("введите значение шага  "))
z = 0
for x in range(x0,x1+dx,dx):
    if x<0: z = x*x
    elif (x>0)and(x<=1): z = sin(x)
    else: z = cos(x)
    print(z)  