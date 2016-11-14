from array_api import Array
import csv

with open('data_example.csv', 'rb') as csv_file:
    reader = csv.reader(csv_file)
    i = 0
    for row in reader:
        print(str(i) + ':' + ','.join(row))
        if row[0] == 'CREATE':
            arr = Array()
        elif row[0] == 'DEBUG':
            arr.debug_print()
        elif row[0] == 'ADD':
            arr.add(row[1])
        elif row[0] == 'INSERT':
            arr.insert(int(row[1]),row[2])
        elif row[0] == 'SET':
            arr.set(int(row[1]),row[2])
        elif row[0] == 'GET':
            arr.get(int(row[1]))
        elif row[0] == 'DELETE':
            arr.delete(int(row[1]))
        elif row[0] == 'SWAP':
            arr.swap(int(row[1]),int(row[2]))
        i += 1