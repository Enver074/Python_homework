# Модуль вывода контактов
def export_data():
    with open('Phonebook\data_base.csv', 'r', encoding='utf-8') as file:
        data = []
        t = []
        for line in file:
            if '|' in line:
                temp = line.strip().split('|')
                data.append(temp)
    return data
