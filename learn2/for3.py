# Оценки
# Создать список из словарей с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
# Посчитать и вывести средний балл по всей школе.
# Посчитать и вывести средний балл по каждому классу.

classroom_scores = [
    {'school_class': '4a', 'scores': [4, 4, 4, 5, 2]},
    {'school_class': '4b', 'scores': [2, 3, 4, 5, 5]},
    {'school_class': '4c', 'scores': [3, 3, 2, 5, 1]},
    {'school_class': '4d', 'scores': [4, 1, 2, 2, 4]}
]
score_sum = 0
sr_sc = 0

for ozenka in classroom_scores:
    ozenka['ozenka_sch']=sum(ozenka['scores'])
    oz= ozenka['ozenka_sch']
    clas = ozenka.get('school_class')
    sr_sc += len(ozenka["scores"])
    score_sum +=oz

print (f'В школе средний балл оценок {score_sum/sr_sc}')    

print()

# Посчитать и вывести средний балл по каждому классу.
for ozenka in classroom_scores:
    ozenka['ozenka_sch']=sum(ozenka['scores'])
    oz= ozenka['ozenka_sch']
    ozenki = len(ozenka["scores"])
    clas = ozenka.get('school_class')     
    print (f'В классе {clas} средний балл {oz/ozenki}')    

