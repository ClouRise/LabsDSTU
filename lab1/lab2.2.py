def find2(n):
    while n>0:
        if n%10==2:
            return "TRUE"
        else:
            n = n//10
    return "FALSE"

n = int(input("введите n  "))
if n < 0:
    print("по условию n > 0")
print(find2(n))