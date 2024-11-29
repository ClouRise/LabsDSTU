def t_ry(N):
    try:
        N = int(N)
    except:
        return False
    else:
        return True
    
def natural(N):
    if t_ry(N) and int(N)>0: return True
    else: 
        print("нужно ввести натуральное число")
        return False

def prnt(N):
    if not natural(N): return False
    else:
        for i in range(1,len(N)+1):
            print(N[-i], end=' ')

N = input("введите натуральное число N:  ")
prnt(N)