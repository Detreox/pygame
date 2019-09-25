def data_connect(username,password):

    import mysql.connector

    mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "Durks.321", database = "login")

    cursor = mydb.cursor()
    cursor = mydb.cursor()
 
    find_user = ("SELECT * FROM user_login WHERE user_name = %s AND user_pass = %s")
    create_user = ("INSERT INTO user_login (user_name, user_pass) VALUES (%s, %s)")

    cursor.execute(find_user, [(username),(password)])
    result = cursor.fetchall()
    if result:
        for i in result:
            print("Welcome Back " + i[1])
            break
    else:
        print("Username and password combination not recognized.")
        answer = input("Would you like to create an account? y/n: \n")
        if answer == "y":
            new_user = input("Enter new Username: ")
            new_pass = input("Enter new Password: ")
            cursor.execute(create_user, [(new_user),(new_pass)])
            mydb.commit()
            cursor.execute(find_user, [(new_user),(new_pass)])
            resultnew = cursor.fetchall()
            if resultnew:
                for j in resultnew:
                    print("Welcome " + j[1])
                    break
        else:
            print("Goodbye!")



    
    
    



