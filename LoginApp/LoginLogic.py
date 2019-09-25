def data_connect():

    import mysql.connector

    mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "Durks.321", database = "login")

    cursor = mydb.cursor()
   

    cursor.execute("select user_name from user_login")
    result = cursor.fetchone()
    

    for i in result:
        print(i)
        
     

    
    
    



