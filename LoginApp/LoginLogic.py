import csv

def user_open():

    with open ('/Users/detreox/Desktop/repo/pygame/LoginApp/users.csv', 'r', encoding= 'utf-8-sig') as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)

user_open()

