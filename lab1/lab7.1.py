mode = input("выберите режим сдвига(1 - вниз, 2 - вправо)  ")
try:
    mode = int(mode)
except(ValueError):
    print("необходимо выбрать число")
else:
    if mode!=1 and mode!=2: print("введите или 1 или 2")
    else:
        #создание пустого списка такого же размера
        s = [[1,2,3],[4,5,6],[7,8,9]]
        dublicate = [0]*len(s)
        for i in range (len(dublicate)):
            dublicate[i] = [0] * len(s[i])

        n = input("насколько сдвигать(выберите число)  ")
        try:
            n = int(n)
        except(ValueError):
            print("необходимо выбрать число")
        else:
            if mode == 2:
                for i in range(len(dublicate)):
                    for j in range(len(dublicate)):
                        dublicate[i][j] = s[i][(j+n-1)%3]
                print(dublicate[0])
                print(dublicate[1])
                print(dublicate[2])
            else:
                for i in range(len(dublicate)):
                    for j in range(len(dublicate)):
                        dublicate[i][j] = s[(i+n-1)%3][j]
                print(dublicate[0])
                print(dublicate[1])
                print(dublicate[2])