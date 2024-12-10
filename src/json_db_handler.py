import json
from types import FunctionType
from typing import Any
from library import Book

class JsonDBNode:

    JsonDB = {}
    DB_file = None

    def __init__(self):
        """Инициализация ДБ и загрузка данных из файла."""

        try:
            with open("lib_data.json", 'r', encoding='utf-8') as file:
                self.JsonDB = json.load(file)  # Чтение и загрузка в Python-объект
                self.DB_file = file
        except FileNotFoundError:
            self.JsonDB = {}  # Если файл отсутствует, присваиваем пустой список
        except json.JSONDecodeError:
            raise json.JSONDecodeError("Файл с данными JSON не исправен") # Если файл неисправен, пробрасываем ошибку наверх

    # def load_books(self):
    #     if not self.JsonDB and not self.DB_file:
    #         self.JsonDB = json.load(self.DB_file)

    #     return self.JsonDB
    
    def save_json_file(self):
        """Сохранение данных в файл."""
        with open("lib_data.json", 'w', encoding='utf-8') as file:
            if self.DB_file == None:
                self.DB_file = file

            json.dump(self.JsonDB, file, ensure_ascii=False, indent=4)  # Сохранение в формате JSON
    
    def add_record(self, record, record_id):
        """Добавление новой записи в JSON-ДБ"""
        self.JsonDB[record_id] = record # установка нумерации, добавление как последнего элемента
        self.save_json_file()

    def delete_record(self, lambda_func:FunctionType):
        """Удаление записи по возвращаемому значению функции."""
        updated_data = [item for item in self.JsonDB if not lambda_func(item)]
        self.save_json_file(updated_data)




if __name__ == "__main__":
    new_json_db = JsonDBNode()

    new_json_db.add_record("abc")

# import json

# def load_json_file(filename):
#     """Загрузка данных из файла."""
#     try:
#         with open(filename, 'r', encoding='utf-8') as file:
#             return json.load(file)  # Чтение и преобразование в Python-объект
#     except FileNotFoundError:
#         return []  # Если файл отсутствует, возвращаем пустой список
#     except json.JSONDecodeError:
#         print("Ошибка декодирования JSON.")
#         return []

# def save_json_file(filename, data):
#     """Сохранение данных в файл."""
#     with open(filename, 'w', encoding='utf-8') as file:
#         json.dump(data, file, ensure_ascii=False, indent=4)  # Сохранение в формате JSON

# def add_record(filename, record):
#     """Добавление новой записи в JSON-файл."""
#     data = load_json_file(filename)
#     data.append(record)
#     save_json_file(filename, data)

# def delete_record(filename, key, value):
#     """Удаление записи по ключу и значению."""
#     data = load_json_file(filename)
#     updated_data = [item for item in data if item.get(key) != value]
#     save_json_file(filename, updated_data)

# # Пример использования
# file_name = 'data.json'

# # Добавление записи
# new_record = {"id": 1, "name": "John Doe", "age": 30}
# add_record(file_name, new_record)

# # Удаление записи по ключу "id" с определённым значением
# delete_record(file_name, "id", 1)

# # Проверка содержимого файла
# print(load_json_file(file_name))