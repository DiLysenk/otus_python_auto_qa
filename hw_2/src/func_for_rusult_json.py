from json import loads, dumps
import csv
from csv import DictReader


with open('../users-39204-8e2f95.json', 'r') as users_file:
    users_file_read = users_file.read()
    users_loads = loads(users_file_read)
    print(users_loads[0])
    print(users_loads[0]['name'])
    print(users_loads[0]['gender'])
    print(users_loads[0]['address'])
    print(items)




with open('../books-39204-271043.csv', 'r') as books_file:
    books_file_read = csv.reader(books_file)


# привести к общему знаменателю, и свести.