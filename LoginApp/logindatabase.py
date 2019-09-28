def login(username, password):

    #MYSQL connector and connection.
    import mysql.connector
    mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "Durks.321", database = "login")

    #Create cursor.
    cursor = mydb.cursor()
 
    #FIND_USER and CREATE_USER MYSQL lines.
    find_user = ("SELECT * FROM user_login WHERE user_name = %s AND user_pass = %s")
    create_user = ("INSERT INTO user_login (user_name, user_pass) VALUES (%s, %s)")
    new_user = ("SELECT * FROM user_login WHERE user_name = %s")

    #Cursor execute find user with username and password from input. Result is fetched.
    cursor.execute(find_user, [(username),(password)])
    result = cursor.fetchall()
    if result:
        for i in result:
            print("Welcome Back " + i[1] + ".")
            break
    else:
        #If username and password does not match, ask user to create a new account.
        print("Username and password combination not recognized.")
        loop = 1
        while loop == 1:
            answer = input("Would you like to create an account? y/n: \n")
            if answer == "y":
                #Ask for new username and password.
                username = input("Enter new Username: ")
                password = input("Enter new Password: ")
                cursor.execute(new_user, [(username)])
                result = cursor.fetchall()
                if result:
                    for k in result:
                        answer = input("Account already exists. Would you like to try again? y/n: \n")
                        if answer == "n":
                            loop = 0
                            print("Goodbye!")
                        break
                else:
                    cursor.execute(create_user, [(username),(password)])
                    mydb.commit()
                    cursor.execute(find_user, [(username),(password)])
                    result = cursor.fetchall()
                    if result:
                        for j in result:
                            print("Welcome " + j[1])
                            break
            else:
                loop = 0
                print("Goodbye!")



    
    
    



