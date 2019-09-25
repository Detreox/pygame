from tkinter import *
from LoginLogic import data_connect

#BUTTON ACTION
def click():
        username = userentry.get()
        password = passentry.get()
        data_connect(username,password)        

#WINDOW
window = Tk()
window.title("Login")

#LABELS
Label (window, text="Username", fg = "black").grid(row = 0, column = 0, sticky = W)
Label (window, text="Password", fg = "black").grid(row = 1, column = 0, sticky = W)

#USERNAME AND PASSWORD ENTRY
userentry = Entry(window, width = 20, bg = "white")
userentry.grid(row = 0, column = 1, sticky = W)
passentry = Entry(window, width = 20, bg = "white")
passentry.grid(row = 1, column = 1, sticky = W)

#LOGIN BUTTON
Button(window, text = "LOGIN", width = 6, command = click).grid(row = 5, column = 1, sticky = W)

window.mainloop() 