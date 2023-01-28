def get_op():
    op = int(input('1 - Добавить студента 2 - Добавить предмет  3 - Добавить оценку  4 - Показать список  5 - Показать конкретный список  6 - Выход'))
    return op

def input_student():
    name = input('Введите имя и фамилию')
    return name
    
def input_lesson():
    less = input('Введите предмет')
    return less

def input_mark():
    name = input('Введи имя')
    less = input('Введи предмет')
    mark = input('Введи оценку')
    return name, less, mark
    
def get_name_to_show():
    name = input('Введи имя')
    return name