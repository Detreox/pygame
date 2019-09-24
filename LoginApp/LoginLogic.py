import csv

def open_csv():
    with open ('/pygame/LoginApp/users.csv', 'r', encoding= 'utf-8-sig') as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)

open_csv()