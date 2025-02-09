n =(input("введите n  "))
try:
    n = float(n)
except(ValueError):
      print("n должно быть числом")
else:
    if float(n) < 0:
        print("по усл   овию n > 0")
    elif int(n)!=n:
        print("n должно быть целым")
    else:
        n = int(n)
        #нормальное решение
        for k in range(n):
            if((k*k)>n):
                print (k)
                break

