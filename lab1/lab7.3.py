Capitals = {
    "Испания" : "Мадрид",
    "Германия" : "Берлин",
    "Россия" : "Москва",
    "Италия" : "Рим",
    "Китай" : "Пекин",
    "Япония" : "Токио"
}
stroka = list(map(str.capitalize, input("Введите текст с названием страны: ").split()))
print(stroka)
for s in stroka:
    if s in Capitals: print("Столица", s, "-",Capitals[s])

