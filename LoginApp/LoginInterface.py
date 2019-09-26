from tkinter import *

import logindatabase


#BUTTON ACTION
def click():
        username = userentry.get()
        password = passentry.get()
        logindatabase.login(username, password)  
        userentry.delete(0, END)
        passentry.delete(0, END)


#WINDOW PANE
window = Tk()
window.title("Login")

#USERNAME LABEL
Label (window, text="Username", fg = "black").grid(row = 0, column = 0, sticky = W)
#PASSWORD LABEL
Label (window, text="Password", fg = "black").grid(row = 1, column = 0, sticky = W)

#USERNAME ENTRY
userentry = Entry(window, width = 20, bg = "white")
userentry.grid(row = 0, column = 1, sticky = W)
#PASSWORD ENTRY
passentry = Entry(window, width = 20, bg = "white")
passentry.grid(row = 1, column = 1, sticky = W)
passentry.config(show = "*")

#LOGIN BUTTON
Button(window, text = "LOGIN", width = 6, command = click).grid(row = 5, column = 1, sticky = W)

window.mainloop() 
