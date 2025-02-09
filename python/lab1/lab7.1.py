from random import *
mode = input("выберите режим сдвига(1 - вниз, 2 - вправо)  ")
N = input("введите длинну матрицы")
M = input("введите ширину матрицы")
try:
    mode = int(mode)
    N  = int(N)
    M  = int(M)
except(ValueError):
    print("необходимо выбрать число")
else:

    if mode!=1 and mode!=2: print("введите или 1 или 2")
    else:
        s = [None]*N
        for i in range (N):
            s[i] = [0] * M
            for j in range(M):
                s[i][j] = randint(-10,10)
        for k in range(N):
            print(s[k])
        #создание пустого списка такого же размера
        dublicate = [0]*N
        for i in range (N):
            dublicate[i] = [0] * M


        n = input("насколько сдвигать(выберите число)  ")
        try:
            n = int(n)
        except(ValueError):
            print("необходимо выбрать число")
        else:
            if mode == 2:
                for i in range(len(dublicate)):
                    for j in range(len(dublicate[i])):
                        dublicate[i][j] = s[i][abs((j-n)%M)]
                for l in range(N):
                    print(dublicate[l])
            else:
                for i in range(len(dublicate)):
                    for j in range(len(dublicate[i])):
                        dublicate[i][j] = s[abs((i-n)%N)][j]
                for l in range(N):
                    print(dublicate[l])
       
                