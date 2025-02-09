def t_ry(N): #проверяем является ли числом 
    try:
        N = int(N)
    except:
        return False
    else:
        return True
    
def natural(N): #проверяем является ли натуральным
    if t_ry(N) and int(N)>0: return True
    else: 
        print("нужно ввести натуральное число")
        return False

def prnt(n,List): #возвращает список цифр
    if len(n)==0: return List
    else:
        List.append(n[-1])
        return prnt (n[:-1], List)

N = input("введите натуральное число N:  ")
if natural(N): print("цифры в обратном порядке: " + " ".join(prnt(N, [])))
