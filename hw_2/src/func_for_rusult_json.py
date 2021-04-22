from json import loads, dumps
import csv
from csv import DictReader

list_users = []
list_books = []
list_total = []

with open('../users-39204-8e2f95.json', 'r') as users_file:
    # прочитаем файл
    users_file_read = users_file.read()
    # прочитаное загрузим в users_loads
    users_loads = loads(users_file_read)

    # найдём целевые значения для name, gender, address.
    for item in users_loads:

        target = [item['name'], item['gender'], item['address']]
        dict_target = dict(zip(['name', 'gender', 'address'], target))
        list_users.append(dict_target)



with open('../books-39204-271043.csv', 'r') as books_file:
    reader = DictReader(books_file)
    header = reader.fieldnames[0:2]
    header.append(reader.fieldnames[3])

    for row in reader:
        title = [row['Title'], row['Author'], row['Height']]
        book = dict(zip(header, title))
        list_books.append(book)


# собираем users и books

for _ in range(len(list_users)):
    if _ <= len(list_books):
        list_users[_].setdefault('books', [list_books[_]])
    else:
        list_users[_].setdefault('books', None)
    list_total.append(list_users[_])




# список с книгами
print('len______--', len(list_users), len(list_books))

j = 0

for i in list_total:
    print(i)

