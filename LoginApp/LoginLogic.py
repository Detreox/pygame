def data_connect():

    import mysql.connector

    mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "Durks.321", database = "login")

    while True:
        username = input("Please enter your username: ")
        password = input("Please etner your password: ")

        cursor = mydb.cursor()

        find_user = ("SELECT * FROM user_login WHERE user_name = %s AND user_pass = %s")
        cursor.execute(find_user, [(username),(password)])
        result = cursor.fetchall()
        if result:
            for i in result:
                print("Welcome " + i[1])
            break
        else:
            print("Username and password combination not recognized.")


    #cursor.execute("select user_name from user_login")


     

    
    
    



