def SumRange(A,B):
    if A>B: return 0
    sum = 0 
    for i in range(A,B+1):
        sum += i
    return sum

A = input("введите число A:  ")
B = input("введите число B:  ")
C = input("введите число C:  ")

try:
    A = int(A)
    B = int(B)
    C = int(C)
except:
    print("нужно ввести целые числа")
else:
    print("сумма от A до B", SumRange(A,B))
    print("сумма от B до C", SumRange(B,C))