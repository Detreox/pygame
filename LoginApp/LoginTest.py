import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Durks.321"
)

print(mydb)

print("Info on database: ")


from LoginLogic import user_open




