from tkinter import *

import logindatabase

#WINDOW PANE
window = Tk()
window.title("Login")
window.geometry("500x400")
window.resizable(0, 0)

#BUTTON ACTION
def log():
        username = userentry.get()
        password = passentry.get()
        logindatabase.login(username, password)
        userentry.delete(0, END)
        passentry.delete(0, END)

def reg():
        register = Tk()
        register.title("Register")
        register.geometry("500x400")
        register.resizable(0, 0)

        #USERNAME LABEL
        Label (register, text="Username", fg = "black").grid(row = 0, column = 2)
        #PASSWORD LABEL
        Label (register, text="Password", fg = "black").grid(row = 1, column = 2)

        userregentry = Entry(register, width = 20, bg = "white")
        userregentry.grid(row = 0, column = 3)

        passregentry = Entry(register, width = 20, bg = "white")
        passregentry.grid(row = 1, column = 3)
        passregentry.config(show = "*")

        Button(window, text = "REGISTER", font=40, width = 6, command = log).grid(row = 5, column = 3)



#USERNAME LABEL
Label (window, text="Username", fg = "black").grid(row = 0, column = 2)
#PASSWORD LABEL
Label (window, text="Password", fg = "black").grid(row = 1, column = 2)

#USERNAME ENTRY
userentry = Entry(window, width = 20, bg = "white")
userentry.grid(row = 0, column = 3)
#PASSWORD ENTRY
passentry = Entry(window, width = 20, bg = "white")
passentry.grid(row = 1, column = 3)
passentry.config(show = "*")

#LOGIN BUTTON
Button(window, text = "LOGIN", font=40, width = 6, command = log).grid(row = 5, column = 3)

#REGISTER BUTTON
Button(window, text = "REGISTER", font=40, width = 6, command = reg).grid(row = 5, column = 5)

window.mainloop()