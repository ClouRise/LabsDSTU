def find2(n):
    while n>0:
        if n%10==2:
            return "TRUE"
        else:
            n = n//10
    return "FALSE"

n = (input("введите n  "))
try:
    n = float(n)
except(ValueError):
      print("n должно быть числом")
else:
    if n < 0:
        print("по условию n > 0")
    elif int(n)!=n:
        print("n должно быть целым")
    else:
        print("Ответ:", find2(int(n)))