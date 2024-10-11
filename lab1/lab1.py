from math import sin, log, tan, exp

#1.

x = int(input())
y = int(input())
z = x**3+2*x**2-5*y
print("z = " + str(z))


#2.

x = int(input())
if x < -2:
    y = (sin(6*x**3))/4*x - x**4
elif x >= 3:
    y = ((2*x**3+4)/5*x**2-2)*tan(2*x+1)
else:
    y = (2*log(x - 1) - exp(x))/8*x+x**2
print(y)
