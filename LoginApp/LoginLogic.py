def data_connect():

    import mysql.connector

    mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "Durks.321", database = "login")

    mycursor = mydb.cursor()

    mycursor.execute("select user_name from user_login")

    for i in mycursor:
        print(i)
