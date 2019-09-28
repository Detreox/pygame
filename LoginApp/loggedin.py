import mysql.connector

def logged():
    
    db = mysql.connector.connect(host = "35.229.93.150", user = "root", passwd = "Durks.321", database = "app_login")
    cursor = db.cursor()

    delete_user = ("DELETE FROM user_login WHERE user_name = %s")

    delete = input("Would you like to delete your account? y/n \n")
    if delete == 'y':
        username = input("Enter your account name to confirm:  \n")
        cursor.execute(delete_user, [(username)])
        db.commit()
    else:
        exit


    
    