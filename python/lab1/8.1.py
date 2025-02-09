def scal(A,B,X,Y):
    return X*A+Y*B

try:
    A = float(input("введите число A:  "))
    B = float(input("введите число B:  "))
    X = float(input("введите число X:  "))
    Y = float(input("введите число Y:  "))
except ValueError:
    print("нужно ввести числа")
else:
    print("скалярное произведение:", scal(A,B,X,Y)) 