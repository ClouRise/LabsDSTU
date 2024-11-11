s = input("введите текст  ")

def splt(s):
    c=1
    for q in range (len(s)):
        if s[q] == ' ':
            c+=1
    a = ['']*c
    r = 0
    for d in range (c):
        for i in range(r,len(s)):
            if s[i] != " ":
                a[d] = a[d] + s[i]
                r += 1
            else:
                r += 1
                break
    t=0 
    for g in range(len(a)):
        if(a[g] != ''):
            t+=1
    y = [None]*t
    m=0
    for o in range(len(y)):
        for v in range(m,len(a)):
            if(a[v]!=''):
                y[o] = a[v]
                m+=1
                break
            else:
                m+=1
    return y


f = splt(s)
print("список", f)
print("кол-во слов:", len(f))