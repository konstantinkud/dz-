# Практика: Сравнение строк
# Написать функцию, которая принимает на вход две строки
# Проверить, является ли то, что передано функции, строками. Если нет - вернуть 0
# Если строки одинаковые, вернуть 1
# Если строки разные и первая длиннее, вернуть 2
# Если строки разные и вторая строка 'learn', возвращает 3
# Вызвать функцию несколько раз, передавая ей разные параметры и выводя на экран результаты

x= input("1 stroka")
y= input("2 stroka")

if (type(x) is int) and (type(y) is int):
    print('0')
elif x == y:
    print("1")     
elif (len(x)>len(y)):
    print("2")    
elif (x != y) and (y == "learn"):
    print("3")
else: 
    print("vse")


