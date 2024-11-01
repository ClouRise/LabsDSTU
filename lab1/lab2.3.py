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
        for k in range(1,n):
            if(n/(k*k)>n):
                print (k)
                break
        print("в задании ошибка так как при делении n на квадрат целого числа мы всегда будем получать число меньшее чем n")
        print("т.е. n/(k*k) < n (всегда)")

        #ну или так

