def scal(A,B,X,Y):
    return X*A+Y*B

A = input("введите число A:  ")
B = input("введите число B:  ")
X = input("введите число X:  ")
Y = input("введите число Y:  ")

try:
    A = float(A)
    B = float(B)
    X = float(X)
    Y = float(Y)
except:
    print("нужно ввести числа")
else:
    print("скалярное произведение:", scal(A,B,X,Y))