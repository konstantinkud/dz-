# Задание
# Создайте словарь:
# {"city": "Москва", "temperature": "20"}
# Выведите на экран значение ключа city
# Уменьшите значение "temperature" на 5
# Выведите на экран весь словарь

word = {"city": "Москва", "temperature": "20"}
print(word["city"])
print(" ")
print(int(word["temperature"])-5 )
print(" ")
print(word)



# Задание
# Проверьте, есть ли в словаре ключ country
# Выведите значение по-умолчанию "Россия" для ключа country
# Добавьте в словарь элемент date со значением "27.05.2019"
# Выведите на экран длину словаря
print("")
print(word.get("country","Россия"))
print('')
word["date"]="27.05.2019"
print(len(word))