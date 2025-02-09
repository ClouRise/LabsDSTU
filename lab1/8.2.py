def SumRange(A,B):
    if A>B: return 0
    sum = 0 
    for i in range(A,B+1):
        sum += i
    return sum

try:
    A = int(input("введите число A:  "))
    B = int(input("введите число B:  "))
    C = int(input("введите число C:  "))
except:
    print("нужно ввести целые числа")
else:
    print("сумма от A до B", SumRange(A,B))
    print("сумма от B до C", SumRange(B,C))3