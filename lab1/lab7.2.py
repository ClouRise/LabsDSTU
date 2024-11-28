from random import *

def dobeautiful(d): #вывод списка
    print("список")
    for i in range(len(d)):
        print(d[i])

N = randint(2,10)
M = randint(2,10)
X = [] # >0
Y = [] # <0
d = [0]*N
for i in range (N):
    d[i] = [0] * M
    for j in range(M):
        d[i][j] = randint(-10,10)
        if d[i][j] > 0:
            X.append(d[i][j])
        elif d[i][j] < 0:
            Y.append(d[i][j])

dobeautiful(d)
print("список положительных чисел",X)
print("список отрицательных чисел",Y)


