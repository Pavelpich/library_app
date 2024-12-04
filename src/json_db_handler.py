import json
from typing import Any

class JsonDBNode:

    JsonDB:list[str] = {}
    DB_file = None

    def __init__(self):
        """Инициализация ДБ и загрузка данных из файла."""

        try:
            with open("lib_data.json", 'r', encoding='utf-8') as file:
                self.JsonDB = json.load(file)  # Чтение и загрузка в Python-объект
        except FileNotFoundError:
            self.JsonDB = []  # Если файл отсутствует, присваиваем пустой список
        except json.JSONDecodeError:
            raise json.JSONDecodeError("Файл с данными JSON не исправен") # Если файл неисправен, пробрасываем ошибку наверх

    def load_books(self) -> list[Book]:
        return json.loads(self.JsonDB, Book)
    
    def save_json_file(filename, data):
        """Сохранение данных в файл."""
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)  # Сохранение в формате JSON
    
    def add_record(self, record):
        """Добавление новой записи в JSON-ДБ"""
        self.JsonDB.append(record)
        self.save_json_file()


if __name__ == "__main__":
    JsonDBNode()

import json

def load_json_file(filename):
    """Загрузка данных из файла."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)  # Чтение и преобразование в Python-объект
    except FileNotFoundError:
        return []  # Если файл отсутствует, возвращаем пустой список
    except json.JSONDecodeError:
        print("Ошибка декодирования JSON.")
        return []

def save_json_file(filename, data):
    """Сохранение данных в файл."""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)  # Сохранение в формате JSON

def add_record(filename, record):
    """Добавление новой записи в JSON-файл."""
    data = load_json_file(filename)
    data.append(record)
    save_json_file(filename, data)

def delete_record(filename, key, value):
    """Удаление записи по ключу и значению."""
    data = load_json_file(filename)
    updated_data = [item for item in data if item.get(key) != value]
    save_json_file(filename, updated_data)

# Пример использования
file_name = 'data.json'

# Добавление записи
new_record = {"id": 1, "name": "John Doe", "age": 30}
add_record(file_name, new_record)

# Удаление записи по ключу "id" с определённым значением
delete_record(file_name, "id", 1)

# Проверка содержимого файла
print(load_json_file(file_name))