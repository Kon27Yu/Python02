'''
1. Создать новый проект
2. (МОДУЛЬ 1) В проекте создать новый модуль variables.py
3. Выбрать объект для описания из списка: овощ, еда, сотрудник, игрушка (так же можно придумать свой)
4. Объявить переменные основных типов данных для описания этого объекта:

Например объект школьник:
имя (тип строка), возраст (тип целое число), класс (тип целое число), отличник или нет (логический тип), средняя оценка (число с плавающей точкой)

Чем больше переменных (характеристик), тем лучше. Минимально 4 переменные для типов (строка, число, число с плавающей точкой, логический тип)

5. В конце модуля с помощью функции type вывести тип для каждой из объявленных переменных
'''
# vegetable
vegetable_name = "cucumber"  # огурец
vegetable_color = "green"  #  цвет - зелёный
vegetable_weight = 100  # вес gr
vegetable_length = 10  # длина cm
vegetable_diameter = 2.5  # диаметр cm
is_vegetable_ripe = True  # зрелый?

print('Name of vegetable:', vegetable_name, type(vegetable_name))
print('Color of vegetable:', vegetable_color, type(vegetable_color))
print('Weight of vegetable:', vegetable_weight, type(vegetable_weight))
print('Length of vegetable:', vegetable_length, type(vegetable_length))
print('Diameter of vegetable:', vegetable_diameter, type(vegetable_diameter))
print('Is vegetable ripe:', is_vegetable_ripe, type(is_vegetable_ripe))
