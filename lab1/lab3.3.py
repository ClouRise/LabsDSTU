from random import *
n = int(input("размер списка:  "))
k = [None]*n
c=0
print(k)
for i in range(n):
    k[i]=randint(-10,10)
    if k[i]==0:
        c+=1
print(k)