  #Setting - Password change, Username change, Background change.
  #Delete User.
import settings
import mysql.connector

def logged():
    
    db = mysql.connector.connect(host = "35.229.93.150", user = "root", passwd = "Durks.321", database = "app_login")
    cursor = db.cursor()

    delete_user = ("DELETE FROM user_login WHERE user_name = %s")

    loop = 1
    while loop == 1:
        print("Main menu: ")
        choice = input("1. Settings \n2. Delete User \n3. Exit \nEnter a Number from the menu: \n")
        if choice == '1':
            loop = 0
            db.close
            settings.setting()
        else:
            if choice == '2':
                loop = 0
                db.close
                user = input("Please enter your username to confirm: \n")
                cursor.execute(delete_user, [(user)])
            else:
                if choice == '3':
                    loop = 0
                    db.close
                    exit
                else:
                    print("Enter one of the numbers listed above.")