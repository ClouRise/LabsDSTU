from random import *
n = int(input("размер списка:  "))
k = [None]*n
c=0
for i in range(n):
    k[i]=randint(-10,10)
    if k[i]==0:
        c+=1
print("кол-во элементов равных 0",k)

def sord(k):
    sord = [None]*len(k)
    mn = 9999999999
    for j in range(len(k)):
        index = 0
        for i in range(len(k)):
            if (k[i] != None) and (abs(k[i]) < abs(mn)):
                mn = k[i]
                index = i
        sord[j] = mn
        dlt(k,index)
        mn = 9999999999
    return sord
def dlt(k,x):
    k[x] = None
print("сортировка по возрастанию модулей", sord(k))
    
        
    
