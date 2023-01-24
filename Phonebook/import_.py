# Модуль записи контакта в фаил
def import_data(data):
    with open('Phonebook\data_base.csv', 'a+', encoding='utf-8') as file:
        for i in data:
            file.write(f"{i}|")
        file.write(f"\n")  

# Модуль ввода контакта в телефонную книгу
def input_data():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    middle_name = input("Введите отчество: ")
    brith_name = input("Введите дату рождения: ")
    phone_number = input("Введите номер контакта: ")
    note = input("Введите комментарий к контакту: ")
    return [last_name, first_name, middle_name, brith_name, phone_number, note]

