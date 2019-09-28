import mysql.connector

def setting():
    db = mysql.connector.connect(host = "35.229.93.150", user = "root", passwd = "Durks.321", database = "app_login")
    cursor = db.cursor()

    find_user = ("SELECT * FROM user_login WHERE user_name = %s")
    change_user = ("UPDATE user_login SET user_name = %s WHERE user_name = %s")

    loop = 1
    while loop == 1:
        
        print("Setttings:\n")
        choice = input("1. Change Username \n2. Change Password \n3. Change Background \nEnter a number from the menu: \n")

        if choice == '1':
            loop = 0
            db.close
            user = input("Enter your username to confirm: \n")
            cursor.execute(find_user, [(user)])
            result = cursor.fetchone()
            for i in result:
                newuser = input("Enter new username: \n")
                cursor.execute(change_user, [(newuser),(user)])
                db.commit()
                break
        else:
            if choice == '2':
                loop = 0
                db.close
                print("Coming Soon.")
            else:
                if choice == '3':
                    loop = 0
                    db.close
                    print("Coming Soon.")
                else:
                    print("Enter one of the numbers listed above.")