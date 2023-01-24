from export import export_data
from print import print_data
# Модуль поиска контакта по ключевому слову
def search_data(word, data):
    if len(data) > 0:
        for item in data:
            if word in item:
                return item
    else:
        return None