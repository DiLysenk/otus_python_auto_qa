import json
from json import loads, dumps
import csv
from csv import DictReader

list_users = [] # список с пользователями
list_books = [] # список с книгами
list_total = [] # результирующий список

with open('../users-39204-8e2f95.json', 'r') as users_file:
    # прочитаем файл с users
    users_file_read = users_file.read()
    # прочитаное загрузим в users_loads
    users_loads = loads(users_file_read)

    # найдём целевые значения для name, gender, address.
    for item in users_loads:

        target = [item['name'], item['gender'], item['address']]
        dict_target = dict(zip(['name', 'gender', 'address'], target))
        # Запишем значения в list_users
        list_users.append(dict_target)



with open('../books-39204-271043.csv', 'r') as books_file:
    # прочитаем файл с books
    reader = DictReader(books_file)
    header = reader.fieldnames[0:2]
    header.append(reader.fieldnames[3])

    for row in reader:
        title = [row['Title'], row['Author'], row['Height']]
        book = dict(zip(header, title))
        # Запишем значения в list_books
        list_books.append(book)


# собираем users и books
for _ in range(len(list_users)):
    if _ <= len(list_books):
        list_users[_].setdefault('books', [list_books[_]])
    else:
        list_users[_].setdefault('books', None)
    list_total.append(list_users[_])

# Записываем файл
with open("result_file.json", 'w') as result_file:
    json.dump(list_total, result_file, indent=2)
