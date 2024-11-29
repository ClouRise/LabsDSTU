def scal(A,B,X,Y):
    return X*A+Y*B

A = input("введите число A:  ")
B = input("введите число B:  ")
X = input("введите число X:  ")
Y = input("введите число Y:  ")

try:
    A = int(A)
    B = int(B)
    X = int(X)
    Y = int(Y)
except:
    print("нужно ввести числа")
else:
    print("скалярное произведение:", scal(A,B,X,Y))